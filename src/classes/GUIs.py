# Import all neccessary modules
import os
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from datetime import datetime
from PIL import Image, ImageTk
import time
import threading
import subprocess
from classes.instruments import SMU
from classes.measurements import dual_channel, read_scope
from classes.instruments import instrument_addresses
from classes.measurements_AP import Noise, TransferFunction



# --- Main Menu Modes ---
class ManualTestingGUI:
    """
    GUI for manual testing mode.
    This GUI allows users to manually control and test various instruments.

    Attributes:
        master: The main application window.

    Methods:
        open_smu: Opens the SMU control window.
        open_sg: Opens the Signal Generator control window.
        open_os: Opens the Oscilloscope control window.
        open_ap: Opens the Audio Precision control window.
    """
    def __init__(self, master):
        master.title("Manual Testing")
        master.resizable(False, False)
        master.minsize(600, 400)
        master.maxsize(600, 400)
        master.configure(bg="#e9ecef")
        style = ttk.Style()
        style.theme_use('clam')
        style.configure('TFrame', background="#ffffff")
        style.configure('TLabel', background="#ffffff", font=("Segoe UI", 12))
        style.configure('Rounded.TButton', font=("Segoe UI", 12, "bold"), padding=[14, 8], borderwidth=2, relief="flat", background="#e3f2fd", foreground="#222")
        style.configure('Accent.Rounded.TButton', font=("Segoe UI", 12, "bold"), padding=[14, 8], borderwidth=2, relief="flat", background="#4CAF50", foreground="white")
        frame = ttk.Frame(master, padding=30, style='TFrame')
        frame.pack(padx=40, pady=40)
        label = ttk.Label(frame, text="Manual Testing Mode", font=("Segoe UI", 16, "bold"), background="#ffffff")
        label.pack(pady=(0, 20))

        def open_smu():
            try:
                smu_win = tk.Toplevel(master)
                SMU_GUI(smu_win)
            except Exception as e:
                messagebox.showerror("Instrument Error", f"SMU is not connected.\nError: {e}")

        def open_sg():
            try:
                sg_win = tk.Toplevel(master)
                SignalGeneratorGUI(sg_win)
            except Exception as e:
                messagebox.showerror("Instrument Error", f"Signal Generator is not connected.\nError: {e}")

        def open_os():
            try:
                os_win = tk.Toplevel(master)
                OscilloscopeGUI(os_win)
            except Exception as e:
                messagebox.showerror("Instrument Error", f"Oscilloscope is not connected.\nError: {e}")

        def open_ap():
            try:
                ap_win = tk.Toplevel(master)
                AudioPrecisionGUI(ap_win)
            except Exception as e:
                messagebox.showerror("Instrument Error", f"Audio Precision is not connected.\nError: {e}")

        btn_ps = ttk.Button(frame, text="SMU", style='Rounded.TButton', command=open_smu)
        btn_ps.pack(pady=10, fill='x')
        btn_sg = ttk.Button(frame, text="Signal Generator", style='Rounded.TButton', command=open_sg)
        btn_sg.pack(pady=10, fill='x')
        btn_os = ttk.Button(frame, text="Oscilloscope", style='Accent.Rounded.TButton', command=open_os)
        btn_os.pack(pady=10, fill='x')
        btn_ap = ttk.Button(frame, text="Audio Precision", style='Accent.Rounded.TButton', command=open_ap)
        btn_ap.pack(pady=10, fill='x')

class AutomatedTestsGUI:
    """
    GUI for automated testing mode.
    This GUI allows users to configure and run automated tests on various instruments.

    Attributes:
        master: The main application window.

    Methods:
        open_noise_vs_freq: Opens the Noise vs Frequency test window.
        open_transfer_function: Opens the Transfer Function test window.
    """
    def __init__(self, master):
        master.title("Automated Tests")
        master.resizable(False, False)
        master.minsize(600, 400)
        master.maxsize(600, 400)
        master.configure(bg="#e9ecef")
        style = ttk.Style()
        style.theme_use('clam')
        style.configure('TFrame', background="#ffffff")
        style.configure('TLabel', background="#ffffff", font=("Segoe UI", 12))
        frame = ttk.Frame(master, padding=30, style='TFrame')
        frame.pack(padx=40, pady=40)
        label = ttk.Label(frame, text="Automated Tests Mode", font=("Segoe UI", 16, "bold"), background="#ffffff")
        label.pack(pady=(0, 20))

        # Add automated testing widgets here
        def open_noise_vs_freq():
            noise_win = tk.Toplevel(master)
            Noise_vs_FrequencyGUI(noise_win)

        def open_transfer_function():
            tf_win = tk.Toplevel(master)
            TransferFunctionGUI(tf_win)


        # Add buttons for each test
        btn_noise = ttk.Button(frame, text="Noise vs Frequency Test", style='Accent.Rounded.TButton', command=open_noise_vs_freq)
        btn_noise.pack(pady=10, fill='x')

        btn_transfer = ttk.Button(frame, text="Transfer Function Test", style='Accent.Rounded.TButton', command=open_transfer_function)
        btn_transfer.pack(pady=10, fill='x')


# -- Automated Testing Widgets --

class Noise_vs_FrequencyGUI:
    """
    GUI for the Noise vs Frequency test.
    This GUI allows users to configure and run the Noise vs Frequency test.

    Attributes:
        master: The main application window.

    Methods:
        start_noise_measurement: Starts the noise measurement process.
    """
    def __init__(self, master):
        self.master = master
        master.title("Noise vs Frequency")
        master.configure(bg="#e9ecef")
        master.resizable(False, False)
        style = ttk.Style()
        style.theme_use('clam')
        style.configure('TFrame', background="#ffffff")
        style.configure('TLabel', background="#ffffff", font=("Segoe UI", 12))
        frame = ttk.Frame(master, padding=30, style='TFrame')
        frame.pack(padx=40, pady=40)
        label = ttk.Label(frame, text="Noise vs Frequency", font=("Segoe UI", 16, "bold"), background="#ffffff")
        label.pack(pady=(0, 20))

        img_path = os.path.join(os.path.dirname(__file__), '..', 'Diagrams', 'Noise_Measurement.png')
        try:
            pil_img = Image.open(img_path)
            self.diagram = ImageTk.PhotoImage(pil_img, master=master)  # Keep reference as self.diagram
            img_frame = ttk.Frame(frame)
            img_frame.pack(pady=10)
            image_label = tk.Label(frame, image=self.diagram)
            image_label.pack(side='left', padx=(0,10))
        except Exception as e:
            err_label = tk.Label(frame, text=f"Could not load diagram: {e}", foreground="red", background="#ffffff")
            err_label.pack(pady=10)

        self.measure_btn = ttk.Button(frame, text="Start Noise Measurement", style='Accent.Rounded.TButton', command=self.start_noise_measurement)
        self.measure_btn.pack(pady=10)


    # Button to start noise measurement
    def start_noise_measurement(self):
        try:
            noise = Noise()
            noise.setup_noise_measurement()
            freqs, noise_vals = noise.run_noise_measurement()
            messagebox.showinfo("Measurement Complete", f"Noise measurement finished.\nFrequencies: {freqs}\nNoise: {noise_vals}")
        except Exception as e:
            messagebox.showerror("Error", f"Noise measurement failed.\n{e}")

class TransferFunctionGUI:
    """
    GUI for the Transfer Function test.
    This GUI allows users to configure and run the Transfer Function test.

    Attributes:
        master: The main application window.

    Methods:
        start_transfer_function_measurement: Starts the transfer function measurement process.
    """
    def __init__(self, master):
        self.master = master
        master.title("Transfer Function")
        master.configure(bg="#e9ecef")
        master.resizable(False, False)
        style = ttk.Style()
        style.theme_use('clam')
        style.configure('TFrame', background="#ffffff")
        style.configure('TLabel', background="#ffffff", font=("Segoe UI", 12))
        frame = ttk.Frame(master, padding=30, style='TFrame')
        frame.pack(padx=40, pady=40)
        label = ttk.Label(frame, text="Transfer Function", font=("Segoe UI", 16, "bold"), background="#ffffff")
        label.pack(pady=(0, 20))

        img_path = os.path.join(os.path.dirname(__file__), '..', 'Diagrams', 'Transfer_Function.png')
        try:
            pil_img = Image.open(img_path)
            self.diagram = ImageTk.PhotoImage(pil_img, master=master)  # Keep reference as self.diagram
            img_frame = ttk.Frame(frame)
            img_frame.pack(pady=10)
            image_label = tk.Label(frame, image=self.diagram)
            image_label.pack(side='left', padx=(0,10))
        except Exception as e:
            err_label = tk.Label(frame, text=f"Could not load diagram: {e}", foreground="red", background="#ffffff")
            err_label.pack(pady=10)

        self.measure_btn = ttk.Button(frame, text="Start Transfer Function Measurement", style='Accent.Rounded.TButton', command=self.start_transfer_function_measurement)
        self.measure_btn.pack(pady=10)


    # Button to start transfer function measurement
    def start_transfer_function_measurement(self):
        try:
            tf = TransferFunction()
            tf.setup_transfer_function_measurement()
            freqs, tf_vals = tf.run_transfer_function_measurement()
            messagebox.showinfo("Measurement Complete", f"Transfer function measurement finished.\nFrequencies: {freqs}\nTransfer Function: {tf_vals}")
        except Exception as e:
            messagebox.showerror("Error", f"Transfer function measurement failed.\n{e}")


# --- Instrument Manual Control GUIs ---

class SMU_GUI:
    """
    GUI for the SMU (Source Measure Unit) control.
    This GUI allows users to configure and control the SMU for various measurements.

    Attributes:
        master: The main application window.

    Methods:
        turn_on: Turns on the SMU.
        turn_off: Turns off the SMU.
    """
    def __init__(self, master):
        self.master = master
        master.title("SMU Control")
        master.configure(bg="#e9ecef")
        master.resizable(False, False)
        style = ttk.Style()
        style.theme_use('clam')
        style.configure('TFrame', background="#ffffff")
        style.configure('TLabel', background="#ffffff", font=("Segoe UI", 12))
        # Softer, more rounded button look
        style.configure('Rounded.TButton', font=("Segoe UI", 12, "bold"), padding=[14, 8], borderwidth=2, relief="flat", background="#e3f2fd", foreground="#222")
        style.map('Rounded.TButton',
            background=[('active', '#bbdefb'), ('!active', '#e3f2fd')],
            relief=[('pressed', 'groove'), ('!pressed', 'flat')],
            bordercolor=[('focus', '#90caf9'), ('!focus', '#e3f2fd')]
        )
        style.configure('Accent.Rounded.TButton', font=("Segoe UI", 12, "bold"), padding=[14, 8], borderwidth=2, relief="flat", background="#4CAF50", foreground="white")
        style.map('Accent.Rounded.TButton',
            background=[('active', '#388E3C'), ('!active', '#4CAF50')],
            relief=[('pressed', 'groove'), ('!pressed', 'flat')],
            bordercolor=[('focus', '#388E3C'), ('!focus', '#4CAF50')]
        )

        self.smu = SMU(instrument_addresses['SMU'])
        self.smu.smu.write_termination = '\n'

        # Main frame
        frame = ttk.Frame(master, padding=20, style='TFrame')
        frame.pack(padx=30, pady=30)

        # Title label with model number
        title = ttk.Label(frame, text="SMU Control (B2901BL)", font=("Segoe UI", 18, "bold"), background="#ffffff")
        title.grid(row=0, column=0, columnspan=2, pady=(0, 18))

        # Voltage
        ttk.Label(frame, text="Voltage (V):").grid(row=1, column=0, sticky='e', padx=10, pady=7)
        self.voltage_entry = ttk.Entry(frame, font=("Segoe UI", 12), width=14)
        self.voltage_entry.grid(row=1, column=1, padx=10, pady=7)

        # Current
        ttk.Label(frame, text="Current limit (µA):").grid(row=2, column=0, sticky='e', padx=10, pady=7)
        self.current_entry = ttk.Entry(frame, font=("Segoe UI", 12), width=14)
        self.current_entry.grid(row=2, column=1, padx=10, pady=7)

        # Time
        ttk.Label(frame, text="Time (s):").grid(row=3, column=0, sticky='e', padx=10, pady=7)
        self.time_entry = ttk.Entry(frame, font=("Segoe UI", 12), width=14)
        self.time_entry.grid(row=3, column=1, padx=10, pady=7)

        # Buttons
        self.on_button = ttk.Button(frame, text="Turn ON", command=self.turn_on, style='Accent.Rounded.TButton')
        self.on_button.grid(row=4, column=0, pady=18, padx=10, sticky='ew')
        self.off_button = ttk.Button(frame, text="Turn OFF", command=self.turn_off, style='Rounded.TButton')
        self.off_button.grid(row=4, column=1, pady=18, padx=10, sticky='ew')

        # Status bar
        self.status = tk.StringVar()
        self.status.set("Ready.")
        status_bar = ttk.Label(master, textvariable=self.status, relief=tk.SUNKEN, anchor='w', background="#f8f9fa", font=("Segoe UI", 10))
        status_bar.pack(fill=tk.X, side=tk.BOTTOM, ipady=3)

    def turn_on(self):
        try:
            voltage = float(self.voltage_entry.get())
            current = float(self.current_entry.get())/1e6
            duration = float(self.time_entry.get())
            if voltage <= 0 or current <= 0 or duration <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Input Error", "Please enter positive numbers for voltage, current, and time.")
            return

        self.smu.smu.write(':SOUR:FUNC:MODE VOLT')
        self.smu.smu.write('VOLT:MODE FIXED')
        self.smu.smu.write('CURR:MODE FIXED')
        self.smu.smu.write(f':SENS:CURR:PROT {current}')
        self.smu.smu.write(f'VOLT {voltage}')
        self.smu.smu.write('OUTP ON')

        self._countdown_time = int(duration)
        self._countdown_active = True
        self._countdown_status(voltage, current)

    def _countdown_status(self, voltage, current):
        if self._countdown_active and self._countdown_time > 0:
            self.status.set(f"Output ON: {voltage} V, {current} A | Time left: {self._countdown_time} s")
            self._countdown_time -= 1
            self.master.after(1000, lambda: self._countdown_status(voltage, current))
        else:
            self.turn_off()

    def turn_off(self):
        self._countdown_active = False
        self.smu.smu.write('OUTP OFF')
        self.smu.smu.write('VOLT 0')
        self.smu.smu.write('CURR 0')
        self.voltage_entry.delete(0, tk.END)
        self.current_entry.delete(0, tk.END)
        self.time_entry.delete(0, tk.END)
        self.status.set("Output OFF.")

class SignalGeneratorGUI:
    """
    GUI for the Signal Generator.
    This GUI allows users to configure and control the Signal Generator for various waveforms.

    Attributes:
        master: The main application window.

    Methods:
        start_signal_generation: Starts the signal generation process.
        stop_signal_generation: Stops the signal generation process.
    """
    def __init__(self, master):
        self.master = master
        master.title("Signal Generator Control")
        master.configure(bg="#e9ecef")
        master.resizable(False, False)
        style = ttk.Style()
        style.theme_use('clam')
        style.configure('TFrame', background="#ffffff")
        style.configure('TLabel', background="#ffffff", font=("Segoe UI", 12))
        style.configure('Rounded.TButton', font=("Segoe UI", 12, "bold"), padding=[14, 8], borderwidth=2, relief="flat", background="#e3f2fd", foreground="#222")
        style.map('Rounded.TButton',
            background=[('active', '#bbdefb'), ('!active', '#e3f2fd')],
            relief=[('pressed', 'groove'), ('!pressed', 'flat')],
            bordercolor=[('focus', '#90caf9'), ('!focus', '#e3f2fd')]
        )
        style.configure('Accent.Rounded.TButton', font=("Segoe UI", 12, "bold"), padding=[14, 8], borderwidth=2, relief="flat", background="#4CAF50", foreground="white")
        style.map('Accent.Rounded.TButton',
            background=[('active', '#388E3C'), ('!active', '#4CAF50')],
            relief=[('pressed', 'groove'), ('!pressed', 'flat')],
            bordercolor=[('focus', '#388E3C'), ('!focus', '#4CAF50')]
        )


        frame = ttk.Frame(master, padding=20, style='TFrame')
        frame.pack(padx=30, pady=30)

        # Title label with model number
        title = ttk.Label(frame, text="Signal Generator Control (33500B)", font=("Segoe UI", 18, "bold"), background="#ffffff")
        title.grid(row=0, column=0, columnspan=2, pady=(0, 18))


        # --- Horizontal stacking of Signal Generator and Clock Generator ---
        h_frame = ttk.Frame(frame, style='TFrame')
        h_frame.grid(row=1, column=0, columnspan=2, sticky='nsew', padx=0, pady=(0, 12))

        # Signal Generator section (left)
        sg_frame = ttk.LabelFrame(h_frame, text="Signal Generator", padding=12, style='TFrame')
        sg_frame.grid(row=0, column=0, sticky='n', padx=(0, 16), pady=0)


        # Input Type (row 0)
        ttk.Label(sg_frame, text="Input Type:").grid(row=0, column=0, sticky='e', padx=10, pady=7)
        self.input_type = tk.StringVar(value='sin')
        input_type_menu = ttk.Combobox(sg_frame, textvariable=self.input_type, values=['sin', 'square', 'DC'], font=("Segoe UI", 12), width=12, state='readonly')
        input_type_menu.grid(row=0, column=1, padx=10, pady=7)

        # Phase Mode (row 1)
        ttk.Label(sg_frame, text="Phase Mode:").grid(row=1, column=0, sticky='e', padx=10, pady=7)
        self.phase_mode = tk.StringVar(value='Antiphase')
        phase_mode_menu = ttk.Combobox(sg_frame, textvariable=self.phase_mode, values=['Antiphase', 'In-phase'], font=("Segoe UI", 12), width=12, state='readonly')
        phase_mode_menu.grid(row=1, column=1, padx=10, pady=7)

        # Duration (row 2)
        ttk.Label(sg_frame, text="Duration (s):").grid(row=2, column=0, sticky='e', padx=10, pady=7)
        self.duration_entry = ttk.Entry(sg_frame, font=("Segoe UI", 12), width=14)
        self.duration_entry.grid(row=2, column=1, padx=10, pady=7)

        # Frequency (row 3)
        ttk.Label(sg_frame, text="Frequency (Hz):").grid(row=3, column=0, sticky='e', padx=10, pady=7)
        self.frequency_entry = ttk.Entry(sg_frame, font=("Segoe UI", 12), width=14)
        self.frequency_entry.grid(row=3, column=1, padx=10, pady=7)

        # Amplitude (row 4)
        ttk.Label(sg_frame, text="Peak-to-Peak Voltage (mV):").grid(row=4, column=0, sticky='e', padx=10, pady=7)
        self.amplitude_entry = ttk.Entry(sg_frame, font=("Segoe UI", 12), width=14)
        self.amplitude_entry.grid(row=4, column=1, padx=10, pady=7)

        # Offset (row 5)
        ttk.Label(sg_frame, text="Offset (mV):").grid(row=5, column=0, sticky='e', padx=10, pady=7)
        self.offset_entry = ttk.Entry(sg_frame, font=("Segoe UI", 12), width=14)
        self.offset_entry.grid(row=5, column=1, padx=10, pady=7)

        # Clock Generator section (right)
        clock_frame = ttk.LabelFrame(h_frame, text="Clock Generator", padding=12, style='TFrame')
        clock_frame.grid(row=0, column=1, sticky='n', padx=(0, 0), pady=0)

        # Enable Clock Generator checkbox inside clock_frame
        self.use_clock = tk.BooleanVar(value=True)
        clock_check = ttk.Checkbutton(clock_frame, text="Enable Clock Generator", variable=self.use_clock, command=self._toggle_clock_fields)
        clock_check.grid(row=0, column=0, columnspan=2, pady=(0, 10), sticky='w')

        ttk.Label(clock_frame, text="Clock Frequency (Hz):").grid(row=1, column=0, sticky='e', padx=10, pady=7)
        self.clock_frequency_entry = ttk.Entry(clock_frame, font=("Segoe UI", 12), width=14)
        self.clock_frequency_entry.grid(row=1, column=1, padx=10, pady=7)

        ttk.Label(clock_frame, text="Clock Amplitude (mV):").grid(row=2, column=0, sticky='e', padx=10, pady=7)
        self.clock_amplitude_entry = ttk.Entry(clock_frame, font=("Segoe UI", 12), width=14)
        self.clock_amplitude_entry.grid(row=2, column=1, padx=10, pady=7)

        ttk.Label(clock_frame, text="Clock Offset (mV):").grid(row=3, column=0, sticky='e', padx=10, pady=7)
        self.clock_offset_entry = ttk.Entry(clock_frame, font=("Segoe UI", 12), width=14)
        self.clock_offset_entry.grid(row=3, column=1, padx=10, pady=7)

        # No clock type selection needed; always square
        self.clock_fields = [
            self.clock_frequency_entry,
            self.clock_amplitude_entry,
            self.clock_offset_entry
        ]

        # Buttons (below the horizontal frame)
        self.start_button = ttk.Button(frame, text="Start", command=self.start_generators, style='Accent.Rounded.TButton')
        self.start_button.grid(row=2, column=0, pady=18, padx=10, sticky='ew')
        self.stop_button = ttk.Button(frame, text="Stop", command=self.stop_generators, style='Rounded.TButton')
        self.stop_button.grid(row=2, column=1, pady=18, padx=10, sticky='ew')

        # Status bar
        self.status = tk.StringVar()
        self.status.set("Ready.")
        status_bar = ttk.Label(self.master, textvariable=self.status, relief=tk.SUNKEN, anchor='w', background="#f8f9fa", font=("Segoe UI", 10))
        status_bar.pack(fill=tk.X, side=tk.BOTTOM, ipady=3)

        self.input_sg = None
        self.clock_sg = None

        # Set initial state of clock fields
        self._toggle_clock_fields()

        # Store references to signal fields for toggling
        self.signal_fields = [self.frequency_entry, self.offset_entry, phase_mode_menu]
        input_type_menu.bind('<<ComboboxSelected>>', lambda e: self._toggle_signal_fields())

    def _toggle_clock_fields(self):
        state = 'normal' if self.use_clock.get() else 'disabled'
        for widget in self.clock_fields:
            widget.config(state=state)

    def _toggle_signal_fields(self):
        # For DC, only Peak-to-Peak Voltage is disabled; offset remains enabled
        if self.input_type.get() == 'DC':
            self.frequency_entry.config(state='disabled')
            self.amplitude_entry.config(state='disabled')
            self.offset_entry.config(state='normal')
            self.signal_fields[2].config(state='disabled')  # phase_mode_menu
        else:
            self.frequency_entry.config(state='normal')
            self.amplitude_entry.config(state='normal')
            self.offset_entry.config(state='normal')
            self.signal_fields[2].config(state='normal')  # phase_mode_menu

    def start_generators(self):
        try:
            duration = float(self.duration_entry.get())
            input_type = self.input_type.get()
            if input_type == 'DC':
                # For DC, only offset is used as the output voltage
                offset = float(self.offset_entry.get())
                amplitude = None
                frequency = None
                if duration <= 0:
                    raise ValueError
            else:
                amplitude = float(self.amplitude_entry.get())
                frequency = float(self.frequency_entry.get())
                offset = float(self.offset_entry.get())
                if duration <= 0 or frequency <= 0:
                    raise ValueError
            use_clock = self.use_clock.get()
            if use_clock:
                clock_frequency = float(self.clock_frequency_entry.get())
                clock_amplitude = float(self.clock_amplitude_entry.get())
                clock_offset = float(self.clock_offset_entry.get())
                if clock_frequency <= 0:
                    raise ValueError
        except ValueError:
            self.status.set("Enter valid positive numbers for all fields.")
            return

        input_type = self.input_type.get()
        phase_mode_value = self.phase_mode.get()
        self.input_sg = dual_channel(instrument_addresses['generator1'], type=input_type, duration=duration)

        def show_double_gui_input(self):
            type_ = self.type
            if type_ == 'DC':
                # For DC, use offset as output voltage
                for num in [1, 2]:
                    self.sg.sg.write(f'SOUR{num}:FUNC {type_}')
                    self.sg.sg.write(f'SOUR{num}:VOLT:OFFS {offset/1000}')
                # No phase, frequency, or amplitude commands for DC
            else:
                for num in [1, 2]:
                    self.sg.sg.write(f'SOUR{num}:FUNC {type_}')
                    self.sg.sg.write(f'SOUR{num}:FREQ {frequency}')
                    self.sg.sg.write(f'SOUR{num}:VOLT {amplitude/1000}')
                    self.sg.sg.write(f'SOUR{num}:VOLT:OFFS {offset/1000}')
                # Set phase according to phase_mode
                if phase_mode_value == 'Antiphase':
                    self.sg.sg.write('SOUR1:PHAS 0')
                    self.sg.sg.write('SOUR2:PHAS 180')
                else:
                    self.sg.sg.write('SOUR1:PHAS 0')
                    self.sg.sg.write('SOUR2:PHAS 0')
                self.sg.sg.write('PHAS:SYNC')
            for num in [1, 2]:
                self.sg.sg.write(f'OUTP{num} ON')
            if type_ != 'DC':
                self.sg.sg.write('PHAS:SYNC')
            time.sleep(self.duration)
            # Only send OFF if not stopped
            if not getattr(self, '_stop_generators', False):
                for num in [1, 2]:
                    self.sg.sg.write(f'OUTP{num} OFF')

        self.input_sg._stop_generators = False
        self.input_sg.show_double = show_double_gui_input.__get__(self.input_sg)

        threads = []
        t1 = threading.Thread(target=self.input_sg.show_double)
        threads.append(t1)

        if self.use_clock.get():
            # Clock type is always 'square'
            self.clock_sg = dual_channel(instrument_addresses['generator2'], type='square', duration=duration)
            def show_double_gui_clock(self):
                type_ = self.type
                for num in [1, 2]:
                    self.sg.sg.write(f'SOUR{num}:FUNC {type_}')
                    self.sg.sg.write(f'SOUR{num}:FREQ {clock_frequency}')
                    self.sg.sg.write(f'SOUR{num}:VOLT {clock_amplitude/1000}')
                    self.sg.sg.write(f'SOUR{num}:VOLT:OFFS {clock_offset/1000}')
                self.sg.sg.write('SOUR1:PHAS 0')
                self.sg.sg.write('SOUR2:PHAS 180')
                self.sg.sg.write('PHAS:SYNC')
                for num in [1, 2]:
                    self.sg.sg.write(f'OUTP{num} ON')
                self.sg.sg.write('PHAS:SYNC')
                time.sleep(self.duration)
                # Only send OFF if not stopped
                if not getattr(self, '_stop_generators', False):
                    for num in [1, 2]:
                        self.sg.sg.write(f'OUTP{num} OFF')
            self.clock_sg._stop_generators = False
            self.clock_sg.show_double = show_double_gui_clock.__get__(self.clock_sg)
            t2 = threading.Thread(target=self.clock_sg.show_double)
            threads.append(t2)
        else:
            self.clock_sg = None

        self._countdown_time = int(duration)
        self._countdown_active = True
        self.start_button.config(state='disabled')
        self._generator_threads = threads
        for t in threads:
            t.start()
        self._update_countdown_status()

    def _update_countdown_status(self):
        if self._countdown_active and self._countdown_time > 0:
            self.status.set(f"Generators running | Time left: {self._countdown_time} s")
            self._countdown_time -= 1
            self.master.after(1000, self._update_countdown_status)
        else:
            # Wait for threads to finish, then re-enable start button
            for t in getattr(self, '_generator_threads', []):
                t.join(timeout=0.1)
            self.start_button.config(state='normal')
            self.status.set("Generators stopped.")

    def stop_generators(self):
        # Stop the countdown and update status immediately
        self._countdown_active = False
        # Set stop flag so threads don't send OFF after close
        if self.input_sg:
            self.input_sg._stop_generators = True
        if self.clock_sg:
            self.clock_sg._stop_generators = True
        # Immediately turn off outputs if possible
        for sg in [self.input_sg, self.clock_sg]:
            if sg and hasattr(sg, 'sg') and hasattr(sg.sg, 'sg'):
                try:
                    sg.sg.sg.write('OUTP1 OFF')
                    sg.sg.sg.write('OUTP2 OFF')
                except Exception:
                    pass
        # Give threads a moment to check the flag
        time.sleep(0.1)
        if self.input_sg:
            self.input_sg.sg.close()
            self.input_sg = None
        if self.clock_sg:
            self.clock_sg.sg.close()
            self.clock_sg = None
        self.master.after(0, lambda: self.status.set("Generators stopped."))

class OscilloscopeGUI:
    """
    GUI for the Oscilloscope control.
    This GUI allows users to configure and control the Oscilloscope for various measurements.

    Attributes:
        master: The main application window.

    Methods:
        read_and_save: Reads data from the oscilloscope and saves it to a file.
    """
    def __init__(self, master):
        self.master = master
        master.title("Oscilloscope Control")
        master.configure(bg="#e9ecef")
        master.resizable(False, False)
        master.minsize(600, 400)
        master.maxsize(600, 400)
        style = ttk.Style()
        style.theme_use('clam')
        style.configure('TFrame', background="#ffffff")
        style.configure('TLabel', background="#ffffff", font=("Segoe UI", 12))
        style.configure('Accent.Rounded.TButton', font=("Segoe UI", 12, "bold"), padding=[14, 8], borderwidth=2, relief="flat", background="#4CAF50", foreground="white")
        style.map('Accent.Rounded.TButton',
            background=[('active', '#388E3C'), ('!active', '#4CAF50')],
            relief=[('pressed', 'groove'), ('!pressed', 'flat')],
            bordercolor=[('focus', '#388E3C'), ('!focus', '#4CAF50')]
        )

        frame = ttk.Frame(master, padding=20, style='TFrame')
        frame.pack(padx=30, pady=30)

        title = ttk.Label(frame, text="Oscilloscope Control (HD304MSO)", font=("Segoe UI", 18, "bold"), background="#ffffff")
        title.pack(pady=(0, 18))

        # Board+Chip label
        label_frame = ttk.Frame(frame, style='TFrame')
        label_frame.pack(pady=6, fill='x')
        ttk.Label(label_frame, text="Board + Chip Label:", font=("Segoe UI", 12), background="#ffffff").pack(side='left', padx=(0,8))
        self.label_entry = ttk.Entry(label_frame, font=("Segoe UI", 12), width=24)
        self.label_entry.pack(side='left', padx=(0,8))

        # Comment box
        comment_frame = ttk.Frame(frame, style='TFrame')
        comment_frame.pack(pady=6, fill='x')
        ttk.Label(comment_frame, text="Comment:", font=("Segoe UI", 12), background="#ffffff").pack(side='left', padx=(0,8))
        self.comment_text = tk.Text(comment_frame, font=("Segoe UI", 12), height=3, width=32)
        self.comment_text.pack(side='left', padx=(0,8))

        # Read Scope button
        self.read_button = ttk.Button(frame, text="Read Scope & Save", command=self.read_and_save, style='Accent.Rounded.TButton')
        self.read_button.pack(pady=12)

        # Status bar
        self.status = tk.StringVar()
        self.status.set("Ready.")
        status_bar = ttk.Label(self.master, textvariable=self.status, relief=tk.SUNKEN, anchor='w', background="#f8f9fa", font=("Segoe UI", 10))
        status_bar.pack(fill=tk.X, side=tk.BOTTOM, ipady=3)

    def read_and_save(self):
        try:
            scope_reader = read_scope()
            data = scope_reader.read()  # Assumes read() returns the scope data as a string or bytes
            label = self.label_entry.get().strip().replace(' ', '_')
            if not label:
                label = "unlabeled"
            today = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            scope_filename = f"scope_{label}_{today}.txt"
            comment_filename = f"scope_{label}_{today}_comments.txt"
            # Save scope output
            with open(scope_filename, "w") as f:
                f.write(data if isinstance(data, str) else data.decode())
            # Save comment
            comment = self.comment_text.get("1.0", tk.END).strip()
            with open(comment_filename, "w") as f:
                f.write(comment)
            self.status.set(f"Scope data saved to {scope_filename}, comment saved to {comment_filename}")
        except Exception as e:
            self.status.set(f"Error: {e}")

class AudioPrecisionGUI:
    """
    GUI for the Audio Precision control.
    This GUI allows users to open the APx500 software for audio analysis and testing.

    Attributes:
        master: The main application window.

    Methods:
        open_api: Opens the APx500 software.
    """
    def __init__(self, master):
        self.master = master
        self.master.title("Audio Precision Control")
        self.master.geometry("600x400")
        self.master.resizable(False, False)
        self.create_widgets()

    def create_widgets(self):
        frame = ttk.Frame(self.master, padding=20)
        frame.pack(fill=tk.BOTH, expand=True)

        title = ttk.Label(frame, text="Audio Precision Control", font=("Segoe UI", 18, "bold"))
        title.pack(pady=(0, 18))

        message = ttk.Label(
            frame,
            text="Manual control is not available in this GUI.\nPlease use the APx500 software already provided for manual Audio Precision control.",
            font=("Segoe UI", 14),
            background="#ffffff",
            foreground="#222",
            wraplength=500,
            justify="center"
        )
        message.pack(pady=40)

        def open_api():
            # Example: Launch APx500 software (update path as needed)
            try:
                subprocess.Popen([r"C:\Program Files\Audio Precision\APx500 9.1\AudioPrecision.APx500.exe"])
            except Exception as e:
                messagebox.showerror("Error", f"Could not open APx500 software.\n{e}")

        btn_api = ttk.Button(frame, text="Open APx500 Software", style='Accent.Rounded.TButton', command=open_api)
        btn_api.pack(pady=10)



'''
# Debug purposes
def initialize_instruments():
    resources = rm.list_resources()
    found = []
    for name, addr in instrument_addresses.items():
        if addr in resources:
            found.append(f"{name} -> ({addr}) \n")
    if found:
        print("Available instruments:\n" + "".join(found))
    else:
        print("No known instruments found.")

initialize_instruments()
'''

'''
class PowerSupplyGUI:
    def __init__(self, master):
        self.master = master
        master.title("Power Supply Control")
        master.configure(bg="#e9ecef")
        master.resizable(False, False)
        style = ttk.Style()
        style.theme_use('clam')
        style.configure('TFrame', background="#ffffff")
        style.configure('TLabel', background="#ffffff", font=("Segoe UI", 12))
        # Softer, more rounded button look
        style.configure('Rounded.TButton', font=("Segoe UI", 12, "bold"), padding=[14, 8], borderwidth=2, relief="flat", background="#e3f2fd", foreground="#222")
        style.map('Rounded.TButton',
            background=[('active', '#bbdefb'), ('!active', '#e3f2fd')],
            relief=[('pressed', 'groove'), ('!pressed', 'flat')],
            bordercolor=[('focus', '#90caf9'), ('!focus', '#e3f2fd')]
        )
        style.configure('Accent.Rounded.TButton', font=("Segoe UI", 12, "bold"), padding=[14, 8], borderwidth=2, relief="flat", background="#4CAF50", foreground="white")
        style.map('Accent.Rounded.TButton',
            background=[('active', '#388E3C'), ('!active', '#4CAF50')],
            relief=[('pressed', 'groove'), ('!pressed', 'flat')],
            bordercolor=[('focus', '#388E3C'), ('!focus', '#4CAF50')]
        )

        self.ps = PowerSupply(instrument_addresses['power_supply'])
        self.ps.ps.write_termination = '\n'

        # Main frame
        frame = ttk.Frame(master, padding=20, style='TFrame')
        frame.pack(padx=30, pady=30)

        # Title label with model number
        title = ttk.Label(frame, text="Power Supply Control (E36311A)", font=("Segoe UI", 18, "bold"), background="#ffffff")
        title.grid(row=0, column=0, columnspan=2, pady=(0, 18))

        # Voltage
        ttk.Label(frame, text="Voltage (V):").grid(row=1, column=0, sticky='e', padx=10, pady=7)
        self.voltage_entry = ttk.Entry(frame, font=("Segoe UI", 12), width=14)
        self.voltage_entry.grid(row=1, column=1, padx=10, pady=7)

        # Current
        ttk.Label(frame, text="Current (A):").grid(row=2, column=0, sticky='e', padx=10, pady=7)
        self.current_entry = ttk.Entry(frame, font=("Segoe UI", 12), width=14)
        self.current_entry.grid(row=2, column=1, padx=10, pady=7)

        # Time
        ttk.Label(frame, text="Time (s):").grid(row=3, column=0, sticky='e', padx=10, pady=7)
        self.time_entry = ttk.Entry(frame, font=("Segoe UI", 12), width=14)
        self.time_entry.grid(row=3, column=1, padx=10, pady=7)

        # Buttons
        self.on_button = ttk.Button(frame, text="Turn ON", command=self.turn_on, style='Accent.Rounded.TButton')
        self.on_button.grid(row=4, column=0, pady=18, padx=10, sticky='ew')
        self.off_button = ttk.Button(frame, text="Turn OFF", command=self.turn_off, style='Rounded.TButton')
        self.off_button.grid(row=4, column=1, pady=18, padx=10, sticky='ew')

        # Status bar
        self.status = tk.StringVar()
        self.status.set("Ready.")
        status_bar = ttk.Label(master, textvariable=self.status, relief=tk.SUNKEN, anchor='w', background="#f8f9fa", font=("Segoe UI", 10))
        status_bar.pack(fill=tk.X, side=tk.BOTTOM, ipady=3)

    def turn_on(self):
        try:
            voltage = float(self.voltage_entry.get())
            current = float(self.current_entry.get())
            duration = float(self.time_entry.get())
            if voltage <= 0 or current <= 0 or duration <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Input Error", "Please enter positive numbers for voltage, current, and time.")
            return

        self.ps.ps.write('VOLT:MODE FIXED')
        self.ps.ps.write('CURR:MODE FIXED')
        self.ps.ps.write(f'VOLT {voltage}')
        self.ps.ps.write(f'CURR {current}')
        self.ps.ps.write('OUTP ON')
        self._countdown_time = int(duration)
        self._countdown_active = True
        self._countdown_status(voltage, current)

    def _countdown_status(self, voltage, current):
        if self._countdown_active and self._countdown_time > 0:
            self.status.set(f"Output ON: {voltage} V, {current} A | Time left: {self._countdown_time} s")
            self._countdown_time -= 1
            self.master.after(1000, lambda: self._countdown_status(voltage, current))
        else:
            self.turn_off()

    def turn_off(self):
        self._countdown_active = False
        self.ps.ps.write('OUTP OFF')
        self.ps.ps.write('VOLT 0')
        self.ps.ps.write('CURR 0')
        self.voltage_entry.delete(0, tk.END)
        self.current_entry.delete(0, tk.END)
        self.time_entry.delete(0, tk.END)
        self.status.set("Output OFF.")
'''










