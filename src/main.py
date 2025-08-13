# main.py
# --- GUI Implementation ---

import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import pyvisa
import time
import threading
from classes.instruments import PowerSupply, SignalGenerator
from classes.measurements import signal_gen, dual_channel

rm = pyvisa.ResourceManager()


instrument_addresses = {
    'power_supply': 'USB0::0x2A8D::0x1002::MY61005055::INSTR',  # Power supply USB address
    'generator1': 'USB0::0x0957::0x2807::MY62003816::INSTR',
    'generator2': 'USB0::0x0957::0x2807::MY62003715::INSTR',
    'oscilloscope': 'USB0::0x2A8D::0x4704::MY65120148::INSTR'  # Oscilloscope USB address
}

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



class PowerSupplyGUI:
    def __init__(self, master):
        self.master = master
        master.title("Power Supply Control")
        master.configure(bg="#e9ecef")

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

        # Title label
        title = ttk.Label(frame, text="Power Supply Control", font=("Segoe UI", 18, "bold"), background="#ffffff")
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


class SignalGeneratorGUI:
    def __init__(self, master):
        self.master = master
        master.title("Signal Generator Control")
        master.configure(bg="#e9ecef")

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

        title = ttk.Label(frame, text="Signal Generator Control", font=("Segoe UI", 18, "bold"), background="#ffffff")
        title.grid(row=0, column=0, columnspan=2, pady=(0, 18))


        # --- Horizontal stacking of Signal Generator and Clock Generator ---
        h_frame = ttk.Frame(frame, style='TFrame')
        h_frame.grid(row=1, column=0, columnspan=2, sticky='nsew', padx=0, pady=(0, 12))

        # Signal Generator section (left)
        sg_frame = ttk.LabelFrame(h_frame, text="Signal Generator", padding=12, style='TFrame')
        sg_frame.grid(row=0, column=0, sticky='n', padx=(0, 16), pady=0)

        ttk.Label(sg_frame, text="Duration (s):").grid(row=0, column=0, sticky='e', padx=10, pady=7)
        self.duration_entry = ttk.Entry(sg_frame, font=("Segoe UI", 12), width=14)
        self.duration_entry.grid(row=0, column=1, padx=10, pady=7)

        ttk.Label(sg_frame, text="Frequency (Hz):").grid(row=1, column=0, sticky='e', padx=10, pady=7)
        self.frequency_entry = ttk.Entry(sg_frame, font=("Segoe UI", 12), width=14)
        self.frequency_entry.grid(row=1, column=1, padx=10, pady=7)

        ttk.Label(sg_frame, text="Amplitude (mV):").grid(row=2, column=0, sticky='e', padx=10, pady=7)
        self.amplitude_entry = ttk.Entry(sg_frame, font=("Segoe UI", 12), width=14)
        self.amplitude_entry.grid(row=2, column=1, padx=10, pady=7)

        ttk.Label(sg_frame, text="Offset (mV):").grid(row=3, column=0, sticky='e', padx=10, pady=7)
        self.offset_entry = ttk.Entry(sg_frame, font=("Segoe UI", 12), width=14)
        self.offset_entry.grid(row=3, column=1, padx=10, pady=7)

        ttk.Label(sg_frame, text="Input Type:").grid(row=4, column=0, sticky='e', padx=10, pady=7)
        self.input_type = tk.StringVar(value='sin')
        input_type_menu = ttk.Combobox(sg_frame, textvariable=self.input_type, values=['sin', 'square'], font=("Segoe UI", 12), width=12, state='readonly')
        input_type_menu.grid(row=4, column=1, padx=10, pady=7)

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

    def _toggle_clock_fields(self):
        state = 'normal' if self.use_clock.get() else 'disabled'
        for widget in self.clock_fields:
            widget.config(state=state)

    def start_generators(self):
        try:
            duration = float(self.duration_entry.get())
            frequency = float(self.frequency_entry.get())
            amplitude = float(self.amplitude_entry.get())
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
        self.input_sg = dual_channel(instrument_addresses['generator1'], type=input_type, duration=duration)

        def show_double_gui_input(self):
            type_ = self.type
            for num in [1, 2]:
                self.sg.sg.write(f'SOUR{num}:FUNC {type_}')
                self.sg.sg.write(f'SOUR{num}:FREQ {frequency}')
                self.sg.sg.write(f'SOUR{num}:VOLT {amplitude/1000}')
                self.sg.sg.write(f'SOUR{num}:VOLT:OFFS {offset/1000}')
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


def main():
    root = tk.Tk()
    root.title("Lab Instrument Automation")
    root.configure(bg="#e9ecef")

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

    frame = ttk.Frame(root, padding=30, style='TFrame')
    frame.pack(padx=40, pady=40)

    title = ttk.Label(frame, text="Lab Instrument Automation", font=("Segoe UI", 20, "bold"), background="#ffffff")
    title.grid(row=0, column=0, columnspan=2, pady=(0, 30))

    def open_ps():
        ps_win = tk.Toplevel(root)
        PowerSupplyGUI(ps_win)

    def open_sg():
        sg_win = tk.Toplevel(root)
        SignalGeneratorGUI(sg_win)

    ps_button = ttk.Button(frame, text="Power Supply Control", command=open_ps, style='Accent.Rounded.TButton', width=22)
    ps_button.grid(row=1, column=0, pady=18, padx=18)
    sg_button = ttk.Button(frame, text="Signal Generator Control", command=open_sg, style='Rounded.TButton', width=22)
    sg_button.grid(row=1, column=1, pady=18, padx=18)

    root.mainloop()

    
if __name__ == "__main__":
    main()
    rm.close()