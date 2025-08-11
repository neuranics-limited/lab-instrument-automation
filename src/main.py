# main.py

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


# --- GUI Implementation ---
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import pyvisa
from classes.instruments import PowerSupply
rm = pyvisa.ResourceManager()


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

def main():
    root = tk.Tk()
    app = PowerSupplyGUI(root)
    root.mainloop()



if __name__ == "__main__":
    main()
    rm.close()



"""
while True: 
    duration = float(input("Enter duration in seconds (0 to exit): "))
    if duration <= 0:
        sg1.sg.close()
        sg2.sg.close()
        break
    else:
        sg1 = dual_channel(instrument_addresses['generator1'], type='square', duration=duration)
        sg2 = dual_channel(instrument_addresses['generator2'], type='sin', duration=duration)
        sg1.show_double()
        sg2.show_double()
"""