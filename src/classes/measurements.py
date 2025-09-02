# Import the neccessary modules
import time
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
from scipy.fft import fft, ifft, fftfreq
import librosa
from typing import Tuple, Optional
import warnings
warnings.filterwarnings('ignore')
from classes.instruments import SignalGenerator, Oscilloscope




class dual_channel():
    """
    A class to handle dual-channel signal generation.

    Attributes:
        sg: An instance of the SignalGenerator class.
        type: The waveform type (e.g., 'SIN', 'SQUARE').
        duration: Duration to output the signal in seconds.

    Methods:
        show_double: Displays the settings for the dual-channel generator.
    """
    def __init__(self, address, type='sin', duration=10):
        self.sg = SignalGenerator(address)
        self.type = type.upper()
        self.duration = duration


    def show_double(self):
        type_ = self.type
        print(f"For generator {self.sg.sg.resource_name}, type is set to {type_}.")
        frequency = float(input("Enter frequency in Hz: "))
        amplitude = float(input("Enter amplitude in mV: "))/1000
        offset = float(input("Enter offset in mV: "))/1000

        for num in [1, 2]:
            self.sg.sg.write(f'SOUR{num}:FUNC {type_}')
            self.sg.sg.write(f'SOUR{num}:FREQ {frequency}')
            self.sg.sg.write(f'SOUR{num}:VOLT {amplitude}')
            self.sg.sg.write(f'SOUR{num}:VOLT:OFFS {offset}')
        self.sg.sg.write('SOUR1:PHAS 0')
        self.sg.sg.write('SOUR2:PHAS 180')
        self.sg.sg.write('PHAS:SYNC')

        for num in [1, 2]:
            self.sg.sg.write(f'OUTP{num} ON')
        time.sleep(self.duration)
        for num in [1, 2]:
            self.sg.sg.write(f'OUTP{num} OFF')


class read_scope():
    """
    A class to handle reading waveforms from an oscilloscope.

    Attributes:
        scope: An instance of the Oscilloscope class.

    Methods:
        read_waveform: Reads the waveform from the oscilloscope.

    Returns:
        waveform: The waveform data read from the oscilloscope.
    """
    def __init__(self, address):
        self.scope = Oscilloscope(address)

    def read_waveform(self, channel=1):
        self.scope.write(f":MEASU:IMMED:TYPe WAVeform")
        self.scope.write(f":MEASU:IMMED:WAVeform:CH{channel} ON")
        waveform = self.scope.read(f":MEASU:IMMED:WAVeform:CH{channel}?")
        return waveform


class TransferFunctionAnalyzer():
    """
    A class to analyze and compute transfer functions between input and output waveforms.
    This is useful for characterizing amplifier or filter responses.

    Attributes:
        sample_rate: The sample rate for audio processing.
        input_signal: The input audio signal.
        output_signal: The output audio signal.
        transfer_function: The computed transfer function.
        frequencies: The frequency bins corresponding to the transfer function.

    Methods:
        load_audio_files: Load input and output audio files.
        set_signals: Set input and output signals directly as numpy arrays.
        compute_transfer_function: Compute the transfer function between input and output signals.
        get_magnitude_response: Get the magnitude response of the transfer function.
        get_phase_response: Get the phase response of the transfer function.
        plot_transfer_function: Plot the transfer function.
        plot_signals_comparison: Plot input and output signals for comparison.
        apply_transfer_function: Apply the transfer function to the input signal.

    Returns:
        Various plots and data depending on the method called.
    """

    def __init__(self, sample_rate: float = 44100):
        self.sample_rate = sample_rate
        self.input_signal = None
        self.output_signal = None
        self.transfer_function = None
        self.frequencies = None

    def load_audio_files(self, input_file: str, output_file: str) -> None:
        """Load input and output audio files."""
        try:
            self.input_signal, sr1 = librosa.load(input_file, sr=self.sample_rate)
            self.output_signal, sr2 = librosa.load(output_file, sr=self.sample_rate)

            # Ensure both signals have the same length
            min_len = min(len(self.input_signal), len(self.output_signal))
            self.input_signal = self.input_signal[:min_len]
            self.output_signal = self.output_signal[:min_len]

            print(f"Loaded audio files successfully")
            print(f"Signal length: {len(self.input_signal)} samples")
            print(f"Duration: {len(self.input_signal) / self.sample_rate:.2f} seconds")

        except Exception as e:
            print(f"Error loading audio files: {e}")

    def set_signals(self, input_signal: np.ndarray, output_signal: np.ndarray) -> None:
        """Set input and output signals directly as numpy arrays."""
        # Ensure both signals have the same length
        min_len = min(len(input_signal), len(output_signal))
        self.input_signal = input_signal[:min_len]
        self.output_signal = output_signal[:min_len]

        print(f"Set signals successfully")
        print(f"Signal length: {len(self.input_signal)} samples")

    def compute_transfer_function(self, method: str = 'fft', window: str = 'hann', 
                                nperseg: Optional[int] = None) -> Tuple[np.ndarray, np.ndarray]:
        """
        Compute the transfer function H(f) = Y(f) / X(f)

        Parameters:
        - method: 'fft' for simple FFT division, 'welch' for Welch's method
        - window: window function for Welch's method
        - nperseg: length of each segment for Welch's method
        """
        if self.input_signal is None or self.output_signal is None:
            raise ValueError("Input and output signals must be set first")

        if method == 'fft':
            return self._compute_fft_transfer_function()
        elif method == 'welch':
            return self._compute_welch_transfer_function(window, nperseg)
        else:
            raise ValueError("Method must be 'fft' or 'welch'")

    def _compute_fft_transfer_function(self) -> Tuple[np.ndarray, np.ndarray]:
        """Compute transfer function using simple FFT division."""
        # Compute FFTs
        X = fft(self.input_signal)
        Y = fft(self.output_signal)

        # Compute transfer function H = Y/X
        # Add small epsilon to avoid division by zero
        epsilon = 1e-10 * np.max(np.abs(X))
        H = Y / (X + epsilon)

        # Generate frequency array
        self.frequencies = fftfreq(len(self.input_signal), 1/self.sample_rate)

        # Only keep positive frequencies
        n_positive = len(self.frequencies) // 2
        self.frequencies = self.frequencies[:n_positive]
        self.transfer_function = H[:n_positive]

        return self.frequencies, self.transfer_function

    def _compute_welch_transfer_function(self, window: str, nperseg: Optional[int]) -> Tuple[np.ndarray, np.ndarray]:
        """Compute transfer function using Welch's method for better noise handling."""
        if nperseg is None:
            nperseg = len(self.input_signal) // 8

        # Compute cross-power spectral density (Pxy) and auto-power spectral density (Pxx)
        f, Pxy = signal.csd(self.input_signal, self.output_signal, 
                           fs=self.sample_rate, window=window, nperseg=nperseg)
        f, Pxx = signal.welch(self.input_signal, fs=self.sample_rate, 
                             window=window, nperseg=nperseg)

        # Transfer function H = Pxy / Pxx
        epsilon = 1e-10 * np.max(Pxx)
        H = Pxy / (Pxx + epsilon)

        self.frequencies = f
        self.transfer_function = H

        return f, H

    def get_magnitude_response(self) -> Tuple[np.ndarray, np.ndarray]:
        """Get magnitude response in dB."""
        if self.transfer_function is None:
            raise ValueError("Transfer function not computed yet")

        magnitude_db = 20 * np.log10(np.abs(self.transfer_function) + 1e-10)
        return self.frequencies, magnitude_db

    def get_phase_response(self) -> Tuple[np.ndarray, np.ndarray]:
        """Get phase response in degrees."""
        if self.transfer_function is None:
            raise ValueError("Transfer function not computed yet")

        phase_deg = np.angle(self.transfer_function, deg=True)
        return self.frequencies, phase_deg

    def plot_transfer_function(self, save_path: Optional[str] = None) -> None:
        """Plot magnitude and phase response of the transfer function."""
        if self.transfer_function is None:
            raise ValueError("Transfer function not computed yet")

        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8))

        # Magnitude response
        freq, mag_db = self.get_magnitude_response()
        ax1.semilogx(freq[1:], mag_db[1:])  # Skip DC component
        ax1.set_xlabel('Frequency (Hz)')
        ax1.set_ylabel('Magnitude (dB)')
        ax1.set_title('Transfer Function - Magnitude Response')
        ax1.grid(True, alpha=0.3)

        # Phase response
        freq, phase_deg = self.get_phase_response()
        ax2.semilogx(freq[1:], phase_deg[1:])  # Skip DC component
        ax2.set_xlabel('Frequency (Hz)')
        ax2.set_ylabel('Phase (degrees)')
        ax2.set_title('Transfer Function - Phase Response')
        ax2.grid(True, alpha=0.3)

        plt.tight_layout()

        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
            print(f"Plot saved to {save_path}")

        plt.show()

    def plot_signals_comparison(self, save_path: Optional[str] = None) -> None:
        """Plot input and output signals for comparison."""
        if self.input_signal is None or self.output_signal is None:
            raise ValueError("Signals not loaded")

        time = np.arange(len(self.input_signal)) / self.sample_rate

        fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(12, 10))

        # Input signal
        ax1.plot(time, self.input_signal, 'b-', alpha=0.7)
        ax1.set_ylabel('Amplitude')
        ax1.set_title('Input Signal (Before Amplification)')
        ax1.grid(True, alpha=0.3)

        # Output signal
        ax2.plot(time, self.output_signal, 'r-', alpha=0.7)
        ax2.set_ylabel('Amplitude')
        ax2.set_title('Output Signal (After Amplification)')
        ax2.grid(True, alpha=0.3)

        # Both signals overlaid
        ax3.plot(time, self.input_signal, 'b-', alpha=0.7, label='Input')
        ax3.plot(time, self.output_signal, 'r-', alpha=0.7, label='Output')
        ax3.set_xlabel('Time (s)')
        ax3.set_ylabel('Amplitude')
        ax3.set_title('Input vs Output Signals')
        ax3.legend()
        ax3.grid(True, alpha=0.3)

        plt.tight_layout()

        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
            print(f"Plot saved to {save_path}")

        plt.show()

    def apply_transfer_function(self, test_signal: np.ndarray) -> np.ndarray:
        """Apply the computed transfer function to a test signal."""
        if self.transfer_function is None:
            raise ValueError("Transfer function not computed yet")

        # Compute FFT of test signal
        X_test = fft(test_signal)
        n_test = len(X_test)

        # Create frequency array for test signal
        freq_test = fftfreq(n_test, 1/self.sample_rate)
        freq_positive_test = freq_test[:n_test//2]

        # Interpolate transfer function to match test signal frequencies
        mag_interp = np.interp(freq_positive_test, self.frequencies, np.abs(self.transfer_function))
        phase_interp = np.interp(freq_positive_test, self.frequencies, np.angle(self.transfer_function))

        # Reconstruct complex transfer function for positive frequencies
        H_positive = mag_interp * np.exp(1j * phase_interp)

        # Mirror for negative frequencies (excluding DC and Nyquist if present)
        if n_test % 2 == 0:  # Even length
            H_full = np.concatenate([H_positive, np.conj(H_positive[-2:0:-1])])
        else:  # Odd length
            H_full = np.concatenate([H_positive, np.conj(H_positive[-1:0:-1])])


        # Ensure both signals have the same length
        min_len = min(len(X_test), len(H_full))
        X_test = X_test[:min_len]
        H_full = H_full[:min_len]

        # Apply transfer function
        Y_test = X_test * H_full

        # Convert back to time domain
        y_test = np.real(ifft(Y_test))

        return y_test






