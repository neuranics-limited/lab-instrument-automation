import numpy as np
import time
from .instruments import PowerSupply, SignalGenerator


class InputOffsetVoltage:
    """
    Automates the measurement of input offset voltage (V_os) for an op-amp or ASIC using a programmable power supply and oscilloscope.

    Methods
    -------
    measure(v_in=0.0, channel=1, n_points=1000, sample_rate=1000):
        Sets the input voltage, measures the output waveform, and returns the typical (84th percentile: mean+std) and maximum offset voltages.
    close():
        Closes the power supply and oscilloscope connections.
    """
    def __init__(self, gain):
        self.gain = gain
        self.ps = PowerSupply()


    def measure(self, voltages=[], currents=[], dwells=[]):
        """
        Sets the voltage, current, and dwell time for the power supply.
        
        Parameters
        ----------
        voltages : list
            List of voltages to set.
        currents : list
            List of currents to set.
        dwells : list
            List of dwell times for each voltage/current setting.
        """
        if len(voltages) != len(currents) or len(voltages) != len(dwells):
            raise ValueError("All input lists must have the same length.")
        
        results = []

        self.ps.write('OUTPUT ON', '(@1)')  # Turn on output for channel 1
        
        for v, c, dwell in zip(voltages, currents, dwells):
            self.ps.write(f'VOLT {v}', '(@1)')  # Set voltage for channel 1
            self.ps.write(f'CURR {c}', '(@1)')  # Set current for channel 1
            print(f'Set V={v}V, I={c}A, waiting {dwell}s...')
            time.sleep(dwell)
            v_meas = float(self.ps.query('MEAS:VOLT?', '(@1)'))  # Measure voltage for channel 1
            v_offset = v_meas / self.gain # Calculate V_offset
            c_meas = float(self.ps.query('MEAS:CURR?', '(@1)'))  # Measure current for channel 1
            print(f'Measured V={v_meas:.4f}V, I={c_meas:.4f}A')
            results.append((v_offset, c_meas))

        with open('src\\data\\input_offset_voltage_data.txt', 'w') as f:
            f.write("V_offset, Current\n")
            for v, c in results:
                f.write(f"{v}, {c}\n")

        '''
        mean = np.mean(v_offset)
        std = np.std(v_offset)
        self.V_typical = mean + 0.47 * std  # 68th percentile
        self.V_max = np.amax(v_offset)  # Maximum output voltage
        '''
        
        self.ps.write('OUTPUT OFF')

    def close(self):
        self.ps.close()
        self.osc.close()
        self.tc.close()

class signal_gen():
    def __init__(self, address):
        self.sg = SignalGenerator(address, timeout=5000)

    def show_single(self):
        if not self.sg.connected:
            print("Failed to connect to Signal Generator.")
            return
        else:
            while True:
                duration = float(input("Enter duration in seconds (0 to exit): "))
                if duration <= 0:
                    self.sg.close()
                    break
                else:
                    type_ = input("Enter signal type (sin, square): ").strip().lower()
                    frequency = float(input("Enter frequency in Hz: "))
                    amplitude = float(input("Enter amplitude in mV: "))
                    offset = float(input("Enter offset in mV: "))
                    if type_== 'sin':
                        self.sg.sin(frequency=frequency, amplitude=amplitude, offset=offset)
                    elif type_ == 'square':
                        self.sg.square(frequency=frequency, amplitude=amplitude, offset=offset)
                    time.sleep(duration)
                    self.sg.sg.write('OUTP OFF')

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