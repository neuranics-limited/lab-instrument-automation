# main.py

import numpy as np
import matplotlib.pyplot as plt
import pyvisa
import time
from classes.instruments import PowerSupply, SignalGenerator
from classes.measurements import InputOffsetVoltage, signal_gen, dual_channel



generator1_address = 'USB0::0x0957::0x2807::MY62003816::0::INSTR' 
generator2_address = 'USB0::0x0957::0x2807::MY62003715::0::INSTR' 
oscilloscope_address = 'USB0::0x2A8D::0x4704::MY65120148::INSTR' #oscilloscope USB address


def main():
    # Initialize VISA resource manager
    rm = pyvisa.ResourceManager()
    resources = rm.list_resources()
    print("Available resources:", resources)
    
    while True: 
        duration = float(input("Enter duration in seconds (0 to exit): "))
        if duration <= 0:
            sg1.sg.close()
            sg2.sg.close()
            break
        else:
            sg1 = dual_channel(generator1_address, type='square', duration=duration)
            sg2 = dual_channel(generator2_address, type='sin', duration=duration)
            sg1.show_double()
            sg2.show_double()
    rm.close()    

if __name__ == "__main__":
    main()



