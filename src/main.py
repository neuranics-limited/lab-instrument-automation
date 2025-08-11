# main.py

import numpy as np
import matplotlib.pyplot as plt
import pyvisa
from time import *
from classes.instruments import PowerSupply, SignalGenerator
from classes.measurements import signal_gen, dual_channel



instrument_addresses = {
    'power_supply': 'USB0::0x2A8D::0x1002::MY61005055::INSTR',  # Power supply USB address
    'generator1': 'USB0::0x0957::0x2807::MY62003816::INSTR',
    'generator2': 'USB0::0x0957::0x2807::MY62003715::INSTR',
    'oscilloscope': 'USB0::0x2A8D::0x4704::MY65120148::INSTR'  # Oscilloscope USB address
}
rm = pyvisa.ResourceManager()

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

def main():
   
    initialize_instruments()

    ps = PowerSupply(instrument_addresses['power_supply'])
    ps.ps.write_termination = '\n'

    voltage = float(input("Enter voltage in V: "))
    current = float(input("Enter current in A: "))
    time = float(input("Enter time in seconds: "))
    if current <= 0:
        print("Invalid current. Exiting.")
        return
    if voltage <= 0:
        print("Invalid voltage. Exiting.")
        return
    ps.ps.write('VOLT:MODE FIXED')  # Set voltage mode to fixed
    ps.ps.write('CURR:MODE FIXED')  # Set current mode to fixed
    ps.ps.write(f'VOLT {voltage}')  # Set voltage
    ps.ps.write('CURR:MODE FIXED')  # Set current mode to fixed
    ps.ps.write(f'CURR {current}') # Set current
    ps.ps.write('OUTP ON')  # Enable power supply output
    sleep(10)  # Wait for the specified time


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