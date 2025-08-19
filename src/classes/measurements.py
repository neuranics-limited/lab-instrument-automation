import time
from classes.instruments import PowerSupply, SignalGenerator, Oscilloscope


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


class read_scope():
    def __init__(self, address):
        self.scope = Oscilloscope(address)

    def read_waveform(self, channel=1):
        self.scope.write(f":MEASU:IMMED:TYPe WAVeform")
        self.scope.write(f":MEASU:IMMED:WAVeform:CH{channel} ON")
        waveform = self.scope.read(f":MEASU:IMMED:WAVeform:CH{channel}?")
        return waveform


