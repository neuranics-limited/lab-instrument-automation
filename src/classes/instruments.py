import numpy as np
import matplotlib.pyplot as plt
import pyvisa


class PowerSupply:
    def __init__(self, address= 'USB0::0x2A8D::0x1002::MY61005055::0::INSTR'):
        self.rm = pyvisa.ResourceManager()
        self.ps = self.rm.open_resource(address)
        self.ps.write_termination = '\n'
        self.ps.write('*RST')
        self.ps.write('*CLS')
        #self.ps.write('OUTP:LOAD INF')
    
    def close(self) -> None:
        self.ps.close()
        self.rm.close()



class SignalGenerator:
    def __init__(self, address):
        self.rm = pyvisa.ResourceManager()
        self.sg = self.rm.open_resource(address)
        self.sg.write_termination = '\n'
        self.sg.write('*RST')
        self.sg.write('*CLS')
        self.sg.write('SYST:BEEP:STAT OFF') # Disable beeping
        self.sg.write('PHAS:SYNC')
        self.sg.write('ROSC:SOUR INT')  
        self.sg.write('TRIG:SOUR BUS')  
        self.sg.write(f'OUTP1:LOAD INF')
        self.sg.write(f'OUTP2:LOAD INF')

    def close(self):
        self.sg.close()

    def sin(self, frequency=1000, amplitude=1.0, offset=0.0, phase=0.0):
        amplitude = amplitude / 1000
        offset = offset / 1000
        self.sg.write(f'APPL:SIN {frequency},{amplitude},{offset}')
        self.sg.write(f'PHAS {phase}')
        

    def square(self, frequency=1000, amplitude=1.0, offset=0.0, phase=0.0):
        amplitude = amplitude / 1000
        offset = offset / 1000
        self.sg.write(f'APPL:SQU {frequency},{amplitude},{offset}')
        self.sg.write(f'PHAS {phase}')
        

    def enable_output(self, enable=True):
        self.sg.write('OUTP ON' if enable else 'OUTP OFF')

