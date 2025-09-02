import pyvisa

instrument_addresses = {
    'power_supply': 'USB0::0x2A8D::0x1002::MY61005055::INSTR',  # Power supply USB address
    'generator1': 'USB0::0x0957::0x2807::MY62003816::INSTR', # Wave generator 1 USB address
    'generator2': 'USB0::0x0957::0x2807::MY62003715::INSTR', # Wave generator 2 USB address
    'oscilloscope': 'USB0::0x2A8D::0x4704::MY65120148::INSTR', # Oscilloscope USB address
    'SMU': 'USB0::0x2A8D::0x9101::MY65150106::INSTR'  # SMU USB address
}




class SMU:
    """
    Class for controlling the Source Measure Unit (SMU) instrument.

    Attributes:
        rm: The resource manager for handling VISA resources.
        smu: The specific SMU instrument resource.

    Methods:
        close: Closes the SMU instrument and the resource manager.
    """
    def __init__(self, address):
        self.rm = pyvisa.ResourceManager()
        self.smu = self.rm.open_resource(address)
        self.smu.write_termination = '\n'
        self.smu.write('*RST')
        self.smu.write('*CLS')

    def close(self):
        self.smu.close()
        self.rm.close()

class SignalGenerator:
    """
    Class for controlling the Signal Generator instrument.

    Attributes:
        rm: The resource manager for handling VISA resources.
        sg: The specific Signal Generator instrument resource.

    Methods:
        close: Closes the Signal Generator instrument and the resource manager.
        sin: Configures the Signal Generator to output a sine wave.
        square: Configures the Signal Generator to output a square wave.
        enable_output: Enables or disables the output of the Signal Generator.
    """

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

class Oscilloscope:
    """
    Class for controlling the Oscilloscope instrument.

    Attributes:
        rm: The resource manager for handling VISA resources.
        scope: The specific Oscilloscope instrument resource.

    Methods:
        close: Closes the Oscilloscope instrument and the resource manager.

    """
    def __init__(self):
        self.rm = pyvisa.ResourceManager()
        self.scope = self.rm.open_resource(instrument_addresses['oscilloscope'])
        self.scope.write_termination = '\n'
        self.scope.read_termination = '\n'
        self.scope.write('*RST')
        self.scope.write('*CLS')
        self.scope.write(f'INP1:LOAD INF')
        self.scope.write(f'INP2:LOAD INF')
        self.scope.write(f'INP3:LOAD INF')
        self.scope.write(f'INP4:LOAD INF')

    def close(self):
        self.scope.close()
        self.rm.close()




'''
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
'''