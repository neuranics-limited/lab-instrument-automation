import pyvisa
import time

rm = pyvisa.ResourceManager()
sg1 = rm.open_resource('USB0::0x0957::0x2707::MY62004362::INSTR')# Secondary gen
sg2 = rm.open_resource('USB0::0x0957::0x2707::MY62004397::0::INSTR')# Primary gen

frequency = 1000
amplitude = 50/1000
offset = 0/1000
phase = 0

def enable_output(sg, enable=True):
        sg.write('OUTP ON' if enable else 'OUTP OFF')

for sg in [sg1, sg2]:
    sg.write_termination = '\n'
    sg.timeout = 5000
    sg.write('*RST')
    sg.write('*CLS')
    idn = sg.query('*IDN?')
    print('*IDN? = ' + idn.rstrip('\n'))

    sg.write('SYST:BEEP:STAT OFF')
    sg.write('PHAS:SYNC')
    sg.write('BURS:STAT ON')
    sg.write('BURS:NCYC INF')
    sg.write('BURS:MODE TRIG')

sg2.write('ROSC:SOUR INT')  # Internal reference for primary
sg2.write('TRIG:SOUR BUS')  # Immediate trigger for primary
sg2.write('TRIG:OUTP ON')

sg1.write('ROSC:SOUR EXT')  # External reference for secondary
sg1.write('TRIG:SOUR EXT')  # External trigger for secondary

for sg in [sg1, sg2]:
    enable_output(sg, False)
    sg.write(f'APPL:SIN {frequency},{amplitude},{offset}')
    sg.write(f'PHAS {phase}')
    sg.write('OUTP:TRIG ON')
    enable_output(sg, True)

sg2.write('*TRG')

time.sleep(6)

for sg in [sg1, sg2]:
    enable_output(sg, False)

