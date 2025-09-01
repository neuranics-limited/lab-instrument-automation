import numpy as np

class InputOffsetVoltage:
    """
    Automates the measurement of input offset voltage (V_os) for an op-amp or ASIC using a programmable power supply and oscilloscope.

    Methods
    -------
    measure(v_in=0.0, channel=1, n_points=1000, sample_rate=1000):
        Sets the input voltage, measures the output waveform, and returns the typical (84th percentile: mean+std) and maximum offset voltages.
    close():
        Closes the power supply and oscilloscope connections.
    """
    def __init__(self, gain):
        self.gain = gain
        self.ps = PowerSupply()


    def measure(self, voltages=[], currents=[], dwells=[]):
        """
        Sets the voltage, current, and dwell time for the power supply.

        Parameters
        ----------
        voltages : list
            List of voltages to set.
        currents : list
            List of currents to set.
        dwells : list
            List of dwell times for each voltage/current setting.
        """
        if len(voltages) != len(currents) or len(voltages) != len(dwells):
            raise ValueError("All input lists must have the same length.")

        results = []

        self.ps.write('OUTPUT ON', '(@1)')  # Turn on output for channel 1

        for v, c, dwell in zip(voltages, currents, dwells):
            self.ps.write(f'VOLT {v}', '(@1)')  # Set voltage for channel 1
            self.ps.write(f'CURR {c}', '(@1)')  # Set current for channel 1
            print(f'Set V={v}V, I={c}A, waiting {dwell}s...')
            time.sleep(dwell)
            v_meas = float(self.ps.query('MEAS:VOLT?', '(@1)'))  # Measure voltage for channel 1
            v_offset = v_meas / self.gain # Calculate V_offset
            c_meas = float(self.ps.query('MEAS:CURR?', '(@1)'))  # Measure current for channel 1
            print(f'Measured V={v_meas:.4f}V, I={c_meas:.4f}A')
            results.append((v_offset, c_meas))

        with open('src\\data\\input_offset_voltage_data.txt', 'w') as f:
            f.write("V_offset, Current\n")
            for v, c in results:
                f.write(f"{v}, {c}\n")

        '''
        mean = np.mean(v_offset)
        std = np.std(v_offset)
        self.V_typical = mean + 0.47 * std  # 68th percentile
        self.V_max = np.amax(v_offset)  # Maximum output voltage
        '''

        self.ps.write('OUTPUT OFF')

    def close(self):
        self.ps.close()
        self.osc.close()
        self.tc.close()

class OpenLoopGain:
    def __init__(self, input_signal, output_signal):
        """
        Automates the A_OL measurement with input and output signals to calculate the gain of the ASIC.

        Parameters
        ----------
        input_signal : array-like
            The input signal waveform.
        output_signal : array-like
            The output signal waveform.
        gain : float
            The gain of the amplifier circuit.
        """


        self.input_signal = input_signal
        self.output_signal = output_signal

    def measure_gain(self):
        """
        Measures the gain of the amplifier circuit by calculating the ratio of output to input signal.

        Returns
        -------
        float
            The calculated gain.
        """
        if len(self.input_signal) != len(self.output_signal):
            raise ValueError("Input and output signals must have the same length.")

        # Calculate gain as the ratio of output to input
        gain_array = self.output_signal / self.input_signal
        gain_mean = np.mean(gain_array)
        gain_std = np.std(gain_array)
        gain_typical = gain_mean +0.47 * gain_std # 68th percentile
        gain_min = np.amin(gain_array)
        gain_currently = gain_mean # Update the global gain variable
        print(gain_currently)
        return gain_typical, gain_min

class GainBandwidthProduct(OpenLoopGain):
    def __init__(self, input_signal, output_signal, frequency=[]):
        """
        Extends OpenLoopGain to calculate the Gain-Bandwidth Product (GBP) of the amplifier.

        Parameters
        ----------
        input_signal : array-like
            The input signal waveform.
        output_signal : array-like
            The output signal waveform.
        frequency : array-like, optional
            The frequency of the input signal. If not provided, it will be calculated based on the input signal.
        """
        super().__init__(input_signal, output_signal)
        self.frequency = frequency if frequency else np.linspace(1, 1000, len(input_signal))
