# main.py

import numpy as np
import matplotlib.pyplot as plt
import pyvisa
import time
from classes.instruments import PowerSupply, SignalGenerator
from classes.measurements import InputOffsetVoltage, signal_gen, double_gen



generator1_address = 'USB0::0x0957::0x2707::MY62004362::INSTR' #secondary generator
generator2_address = 'USB0::0x0957::0x2707::MY62004397::0::INSTR' #primary generator
oscilloscope_address = 'USB0::0x2A8D::0x4704::MY65120148::INSTR' #oscilloscope USB address


def main():
    # Initialize VISA resource manager
    rm = pyvisa.ResourceManager()
    resources = rm.list_resources()
    print("Available resources:", resources)
    
    test2 = SignalGenerator(generator2_address)
    #test1 = SignalGenerator(generator1_address)

    test2.sg.write("APPL:SIN 1e5,0.05,0,0")
    #test1.sg.write("APPL:SIN 1e5,0.05,0,0")
    test2.sg.write('ROSC:SOUR INT')
    #test1.sg.write('ROSC:SOUR EXT')
    test2.sg.write("BURS:MODE TRIG; NCYC 3; PHAS 0")
    #test1.sg.write("BURS:MODE TRIG; NCYC 3; PHAS 180")
    test2.sg.write("TRIG:SOUR BUS; SLOP POS")
    #test1.sg.write("TRIG:SOUR EXT")
    test2.sg.write("BURS:STAT ON")
    #test1.sg.write("BURS:STAT ON")
    test2.sg.write("OUTP 1")


    time.sleep(10)

    test2.close()
    #test1.close()

    #gen = double_gen(addr_primary=generator2_address,
                    #addr_secondary=generator1_address,
                    #type_='sin', frequency=1000, amplitude=100, offset=0)

    #gen.show_double()
    
    #gen.close()




    
    

if __name__ == "__main__":
    main()



