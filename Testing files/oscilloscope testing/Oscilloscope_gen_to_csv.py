import pyvisa
import time
import numpy as np
import os

# Addresses
gen_address  = 'USB0::0x0957::0x2707::MY62004397::0::INSTR'
osc_address = 'USB0::0x2A8D::0x4704::MY65120148::INSTR'

# Output file path (same directory as this script)
output_file = os.path.join(os.path.dirname(__file__), 'oscilloscope_capture.csv')
# Set up generator: 2 kHz, 1 Vpp sine wave or arbitrary waveform
arb_file = os.path.join(os.path.dirname(__file__), 'arb_waveform.csv')
use_arb = os.path.exists(arb_file)

rm = pyvisa.ResourceManager()


with rm.open_resource(gen_address) as gen:
    gen.write_termination = '\n'
    gen.timeout = 5000
    gen.write('*RST')
    gen.write('*CLS')
    if use_arb:
        # Load arbitrary waveform from CSV (expects one column of floats, normalized -1 to 1)
        arb_data = np.loadtxt(arb_file, delimiter=',')
        arb_data = np.clip(arb_data, -1, 1)
        arb_data_int = ((arb_data + 1) * 8191.5).astype(int)  # 0 to 16383 for 14-bit
        arb_str = ','.join(str(val) for val in arb_data_int)
        gen.write('DATA VOLATILE,' + arb_str)
        gen.write('FUNC:USER VOLATILE')
        gen.write('FUNC:SHAP USER')
        gen.write('VOLT 0.05')  # 1 Vpp
        gen.write('FREQ 2000')  # 2 kHz
        print('Arbitrary waveform loaded and outputting.')
    else:
        gen.write('APPL:SIN 2000,0.05,0')  # 2 kHz, 1 Vpp (0.05 V amplitude), 0 V offset
        gen.write('OUTP ON')
        print('Sine wave outputting.')
    


# Set up oscilloscope and acquire waveform
with rm.open_resource(osc_address) as osc:
    osc.write_termination = '\n'
    osc.timeout = 10000
    osc.write('*RST')
    osc.write('*CLS')
    osc.write(':STOP')
    osc.write(':WAV:FORM ASCii')
    osc.write(':WAV:SOUR CHAN1')
    osc.write(':RUN')
    time.sleep(0.5)
    osc.write(':SING')
    time.sleep(1)
    osc.write(':WAV:POIN:MODE RAW')
    osc.write(':WAV:POIN 1000')
    data = osc.query(':WAV:DATA?')
    # Get preamble for scaling
    preamble = osc.query(':WAV:PRE?')
    print('Oscilloscope preamble:', preamble)
    # Save data to file
    with open(output_file, 'w') as f:
        f.write(data)
    print(f'Waveform data saved to {output_file}')
