import pyvisa
import time

def enable_output(sg, enable=True):
    sg.write('OUTP ON' if enable else 'OUTP OFF')

# Instrument addresses (update if needed)
PRIMARY_ADDR = 'USB0::0x0957::0x2707::MY62004397::0::INSTR'
SECONDARY_ADDR = 'USB0::0x0957::0x2707::MY62004362::INSTR'

# Signal parameters
frequency = 1000  # Hz
amplitude = 0.05  # V (50 mV)
offset = 0.0      # V
num_cycles = 20   # Burst cycles

rm = pyvisa.ResourceManager()
sg1 = rm.open_resource(SECONDARY_ADDR)  # Secondary generator
sg2 = rm.open_resource(PRIMARY_ADDR)    # Primary generator

for sg in [sg1, sg2]:
    sg.write_termination = '\n'
    sg.timeout = 5000
    sg.write('*RST')
    sg.write('*CLS')
    print(f"*IDN? = {sg.query('*IDN?').strip()}")
    sg.write('SYST:BEEP:STAT OFF')

# Reference and trigger setup
sg2.write('ROSC:SOUR INT')   # Primary: internal reference
sg2.write('TRIG:SOUR IMM')   # Primary: immediate trigger
sg1.write('ROSC:SOUR EXT')   # Secondary: external reference
sg1.write('TRIG:SOUR EXT')   # Secondary: external trigger

print('Waiting for reference lock...')
time.sleep(1)

# Waveform and burst setup
for sg in [sg1, sg2]:
    enable_output(sg, False)
    sg.write(f'APPL:SIN {frequency},{amplitude},{offset}')
    sg.write('BURS:STAT ON')
    sg.write(f'BURS:NCYC {num_cycles}')
    sg.write('BURS:MODE TRIG')

# Set phase: primary 0°, secondary 180°
sg2.write('PHAS 0')
sg1.write('PHAS 180')

# Sync phase
for sg in [sg1, sg2]:
    sg.write('PHAS:SYNC')

# Enable outputs
enable_output(sg1, True)
enable_output(sg2, True)

print('Waiting for outputs to settle...')
time.sleep(0.5)

sg2.write('*TRIG')

# Wait for burst to complete
print('Waiting for burst...')
time.sleep(3)

# Disable outputs
for sg in [sg1, sg2]:
    enable_output(sg, False)

print('Done.')