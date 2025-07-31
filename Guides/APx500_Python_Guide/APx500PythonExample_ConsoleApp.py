import clr 
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

# Configure the analyzer input and output. The example connectors may not be available on your analyzer.
APx.SignalPathSetup.OutputConnector.Type = OutputConnectorType.AnalogBalanced
APx.SignalPathSetup.InputConnector.Type = InputConnectorType.AnalogBalanced 
APx.SignalPathSetup.Measure = MeasurandType.Acoustic
input1 = APx.SignalPathSetup.InputSettings(APxInputSelection.Input1)
input1.Channels[0].Name = "Mic"
input1.Channels[0].Sensitivity.Value = 0.011

# Add and configure an Acoustic Response measurement
APx.AddMeasurement("Signal Path1", MeasurementType.AcousticResponse)
APx.AcousticResponse.GeneratorWithPilot.Frequencies.Start.Value = 100;
APx.AcousticResponse.GeneratorWithPilot.Frequencies.Stop.Value = 10000;
APx.AcousticResponse.GeneratorWithPilot.Durations.Sweep.Value = 1;
        
#Check a couple results to be included in the active sequence
APx.AcousticResponse.Phase.Checked = True
APx.AcousticResponse.ThdRatio.Checked = True

#Add a derived result and configure it
smooth = APx.AcousticResponse.Level.AddDerivedResult(MeasurementResultType.Smooth).Result.AsSmoothResult();
smooth.OctaveSmoothing = OctaveSmoothingType.Octave3
smooth.Name = "Smoothed Response"
smooth.Checked = True

#Add an export data sequence step to automatically export the smoothed data when the measurement is run in a sequence.
exportStep = APx.AcousticResponse.SequenceMeasurement.SequenceSteps.ExportResultDataSteps.Add()
exportStep.ResultName = smooth.Name
exportStep.ExportSpecification = "All Points"
exportStep.FileName = "$(MyDocuments)\\SmoothedResponse.xlsx"
exportStep.Append = False

# Run the sequence, which will run the Acoustic Response measurement
APx = APx500_Application()
APx.Sequence.Run()
      
# Get results acquired in the last sequence run

# Get Frequency Response RMS Level XY values by result name (string)
level_xvalues = APx.Sequence[0]["Acoustic Response"].SequenceResults["Smoothed Response"].GetXValues(InputChannelIndex.Ch1, VerticalAxis.Left, SourceDataType.Measured, 1)
level_yvalues = APx.Sequence[0]["Acoustic Response"].SequenceResults["Smoothed Response"].GetYValues(InputChannelIndex.Ch1, VerticalAxis.Left, SourceDataType.Measured, 1)

# Get Frequency Response Gain XY values by result type
thd_xvalues = APx.Sequence[0]["Acoustic Response"].SequenceResults[MeasurementResultType.ThdRatioVsFrequency].GetXValues(InputChannelIndex.Ch1, VerticalAxis.Left, SourceDataType.Measured, 1)
thd_yvalues = APx.Sequence[0]["Acoustic Response"].SequenceResults[MeasurementResultType.ThdRatioVsFrequency].GetYValues(InputChannelIndex.Ch1, VerticalAxis.Left, SourceDataType.Measured, 1)

# Convert .NET arrays to Python lists if needed
level_x = list(level_xvalues)
level_y = list(level_yvalues)
thd_x = list(thd_xvalues)
thd_y = list(thd_yvalues)

plt.figure(figsize=(10, 5))
plt.plot(level_x, level_y, label='Smoothed Response (Level)')
plt.plot(thd_x, thd_y, label='THD Ratio vs Frequency')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Level / THD')
plt.title('APx500 Acoustic Response Results')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()