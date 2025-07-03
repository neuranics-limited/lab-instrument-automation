# main.py

import numpy as np
import matplotlib.pyplot as plt
import pyvisa
from classes.instruments import PowerSupply, SignalGenerator
from classes.measurements import InputOffsetVoltage, signal_gen, double_gen

generator1_address = 'USB0::0x0957::0x2707::MY62004362::INSTR' #secondary generator
generator2_address = 'USB0::0x0957::0x2707::MY62004397::0::INSTR' #primary generator


def main():
    # Initialize VISA resource manager
    rm = pyvisa.ResourceManager()
    resources = rm.list_resources()
    print("Available resources:", resources)
    


    gen = double_gen(addr_primary=generator2_address,
                    addr_secondary=generator1_address,
                    type_='sin', frequency=1000, amplitude=50, offset=0)
    
   
    error = gen.primary.sg.query('SYST:ERR?')
    print("Primary instrument error:", error)
    error = gen.secondary.sg.query('SYST:ERR?')
    print("Secondary instrument error:", error)
    
    gen.show_double()
    
    error = gen.primary.sg.query('SYST:ERR?')
    print("Primary instrument error:", error)
    error = gen.secondary.sg.query('SYST:ERR?')
    print("Secondary instrument error:", error)
    
    gen.close()


    
    

if __name__ == "__main__":
    main()



