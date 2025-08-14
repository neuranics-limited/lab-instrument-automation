import time
from classes.instruments import SignalGenerator


class dual_channel():
    def __init__(self, address, type='sin', duration=10):
        self.sg = SignalGenerator(address)
        self.type = type.upper()
        self.duration = duration


    def show_double(self):
        type_ = self.type
        print(f"For generator {self.sg.sg.resource_name}, type is set to {type_}.")
        frequency = float(input("Enter frequency in Hz: "))
        amplitude = float(input("Enter amplitude in mV: "))/1000
        offset = float(input("Enter offset in mV: "))/1000

        for num in [1, 2]:
            self.sg.sg.write(f'SOUR{num}:FUNC {type_}')
            self.sg.sg.write(f'SOUR{num}:FREQ {frequency}')
            self.sg.sg.write(f'SOUR{num}:VOLT {amplitude}')
            self.sg.sg.write(f'SOUR{num}:VOLT:OFFS {offset}')
        self.sg.sg.write('SOUR1:PHAS 0')
        self.sg.sg.write('SOUR2:PHAS 180')
        self.sg.sg.write('PHAS:SYNC')

        for num in [1, 2]:
            self.sg.sg.write(f'OUTP{num} ON')
        time.sleep(self.duration)
        for num in [1, 2]:
            self.sg.sg.write(f'OUTP{num} OFF')