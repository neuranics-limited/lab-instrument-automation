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
APx.SignalPathSetup.Measure = MeasurandType.Voltage

# Set up input channel for sensor
input1 = APx.SignalPathSetup.InputSettings(APxInputSelection.Input1)
input1.Channels[0].Name = "Sensor"

# Add SIGNAL ANALYZER measurement for noise analysis (not FrequencyResponse)
APx.AddMeasurement("Signal Path1", MeasurementType.SignalAnalyzer)

# Configure signal analyzer for noise measurement
APx.SignalAnalyzer.FrequencySpan.Value = 1000.0  # 1 kHz span
APx.SignalAnalyzer.StartFrequency.Value = 1.0    # Start at 1 Hz
APx.SignalAnalyzer.AverageCount = 10             # Average for noise reduction

# DISABLE generator - we want to measure noise, not response
APx.Generator.OutputEnabled = False

# Enable voltage noise density result
APx.SignalAnalyzer.Results[MeasurementResultType.VoltageNoiseDensity].Enabled = True

print("Starting voltage noise density measurement...")

# Run the measurement
APx.Sequence.Run()

# Wait for completion
while APx.Sequence.IsRunning:
    time.sleep(0.1)

# Get noise density results
noise_result = APx.Sequence[0]["Signal Analyzer"].SequenceResults[MeasurementResultType.VoltageNoiseDensity]
frequencies = list(noise_result.GetXValues(InputChannelIndex.Ch1, VerticalAxis.Left, SourceDataType.Measured, 1))
noise_levels = list(noise_result.GetYValues(InputChannelIndex.Ch1, VerticalAxis.Left, SourceDataType.Measured, 1))

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

