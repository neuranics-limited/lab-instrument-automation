import pyvisa
import time


rm  = pyvisa.ResourceManager()
print(rm.list_resources())
address = 'USB0::0x2A8D::0x9101::MY65150106::INSTR'

smu = rm.open_resource(address)



smu.write_termination = '\n'
smu.write("*RST")
smu.write("*CLS")

# Turn on

voltage_entry = input("Enter voltage (V): ")
current_entry = input("Enter current limit (microA): ")
duration_entry = input("Enter duration (s): ")

try:
    voltage = float(voltage_entry)
    current = float(current_entry) / 1e6  # Convert microA to A
    duration = float(duration_entry)
    if voltage <= 0 or current <= 0 or duration <= 0:
            raise ValueError
except ValueError:
    print("Please enter valid positive numbers for voltage, current, and duration.")


smu.write('OUTP ON')

smu.write(':SOUR:FUNC:MODE VOLT')
smu.write('VOLT:MODE FIXED')
smu.write('CURR:MODE FIXED')

smu.write(f':SENS:CURR:PROT {current}')
smu.write(f'VOLT {voltage}')

smu.write('OUTP ON')


time.sleep(duration)

# Turn off
smu.write('VOLT 0')
smu.write('CURR 0')
smu.write('OUTP OFF')


smu.close()