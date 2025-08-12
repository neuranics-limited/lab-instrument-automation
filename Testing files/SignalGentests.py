import pyvisa
from classes.instruments import PowerSupply, SignalGenerator
from classes.measurements import signal_gen, dual_channel
rm = pyvisa.ResourceManager()

instrument_addresses = {
    'power_supply': 'USB0::0x2A8D::0x1002::MY61005055::INSTR',  # Power supply USB address
    'generator1': 'USB0::0x0957::0x2807::MY62003816::INSTR',
    'generator2': 'USB0::0x0957::0x2807::MY62003715::INSTR',
    'oscilloscope': 'USB0::0x2A8D::0x4704::MY65120148::INSTR'  # Oscilloscope USB address
}



while True: 
    duration = float(input("Enter duration in seconds (0 to exit): "))
    if duration > 0:
        input_sg = dual_channel(instrument_addresses['generator1'], type='sin', duration=duration)
        clock_sg = dual_channel(instrument_addresses['generator2'], type='square', duration=duration)
        input_sg.show_double()
        clock_sg.show_double()
    else:
        input_sg.sg.close()
        break
