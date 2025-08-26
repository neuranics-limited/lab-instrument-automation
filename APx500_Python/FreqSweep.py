import clr
import numpy as np
import time
import matplotlib.pyplot as plt

# Add a reference to the APx API
clr.AddReference(r"C:\Program Files\Audio Precision\APx500 9.1\API\AudioPrecision.API3.dll")
clr.AddReference(r"C:\Program Files\Audio Precision\APx500 9.1\API\AudioPrecision.API2.dll")
clr.AddReference(r"C:\Program Files\Audio Precision\APx500 9.1\API\AudioPrecision.API.dll")
from AudioPrecision.API import *

# Instantiate and create a new project
APx = APx500_Application()
APx.Visible = True
APx.CreateNewProject()

# Configure for noise measurement
APx.SignalPathSetup.InputConnector.Type = InputConnectorType.AnalogBalanced
APx.SignalPathSetup.OutputConnector.Type = OutputConnectorType.AnalogBalanced
APx.SignalPathSetup.Measure = MeasurandType.Voltage
# Set up input channel for sensor
input1 = APx.SignalPathSetup.InputSettings(APxInputSelection.Input1)
input1.Channels[0].Name = "Sensor"


# Add SIGNAL ANALYZER measurement for noise analysis (not FrequencyResponse)
APx.AddMeasurement("Signal Path1", MeasurementType.SignalAnalyzer)  # INoiseRecorderMeasurement
APx.SignalAnalyzer.AcquisitionSeconds = 5.0 # Set acquisition time
APx.SignalAnalyzer.AcquisitionType = AcqLengthType.Seconds  # or .Auto
APx.SignalAnalyzer.Averages = 10  # Set number of averages for noise reduction

APx.SignalAnalyzer.AnalogInputBandwidth = SignalAnalyzerBandwidthType.Bw20k44kHz  # Example: 20 kHz to 44 kHz bandwidth, check your API for available enums

# Add a derived result and configure it
noise_result = APx.SignalAnalyzer.AmplitudeSpectralDensity.Result.AsXYGraph()
noise_result.Name = "Voltage Noise Density"
noise_result.Checked = True


print("Starting voltage noise density measurement...")

# Run the measurement
APx = APx500_Application()
APx.Sequence.Run()

# Wait for completion
while APx.Sequence.IsRunning:
    print("Waiting for measurement to complete...")
    time.sleep(0.1)


frequencies = list(APx.Sequence[0]["Signal Path1"].SequenceResults["Voltage Noise Density"].GetXValues(InputChannelIndex.Ch1, VerticalAxis.Left, SourceDataType.Measured, 1))
noise_levels = list(APx.Sequence[0]["Signal Path1"].SequenceResults["Voltage Noise Density"].GetYValues(InputChannelIndex.Ch1, VerticalAxis.Left, SourceDataType.Measured, 1))


cutoff_frequency = int(input("Enter cutoff frequency in Hz: "))   # Example cutoff frequency in Hz
frequencies = [f for f in frequencies if f < cutoff_frequency]
noise_levels = [n for n, f in zip(noise_levels, frequencies) if f < cutoff_frequency]

# Plot results
plt.figure(figsize=(10, 6))
plt.loglog(frequencies, noise_levels, 'b-', label='Measured')
plt.xlabel('Frequency [Hz]')
plt.ylabel('Voltage noise density [V/√Hz]')
plt.title('Voltage noise measurement')
plt.grid(True, which="both", ls="-", alpha=0.3)
plt.legend()
plt.show()

# Save data
np.savetxt('voltage_noise_data.csv', np.column_stack([frequencies, noise_levels]),
           delimiter=',', header='Frequency_Hz,Noise_V_per_sqrt_Hz')

print("Measurement complete. Data saved to voltage_noise_data.csv")

