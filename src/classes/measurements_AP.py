import clr
import time


# Add a reference to the APx API
clr.AddReference(r"C:\Program Files\Audio Precision\APx500 9.1\API\AudioPrecision.API3.dll")
clr.AddReference(r"C:\Program Files\Audio Precision\APx500 9.1\API\AudioPrecision.API2.dll")
clr.AddReference(r"C:\Program Files\Audio Precision\APx500 9.1\API\AudioPrecision.API.dll")
from AudioPrecision.API import *



class Noise:

    def __init__(self):
        self.APx = APx500_Application()
        self.APx.Visible = True
        self.APx.CreateNewProject()

    def setup_noise_measurement(self):
        # Configure for noise measurement
        self.APx.SignalPathSetup.InputConnector.Type = InputConnectorType.AnalogBalanced
        self.APx.SignalPathSetup.OutputConnector.Type = OutputConnectorType.AnalogBalanced
        self.APx.SignalPathSetup.Measure = MeasurandType.Voltage
        input1 = self.APx.SignalPathSetup.InputSettings(APxInputSelection.Input1)
        input1.Channels[0].Name = "Sensor"

        # Add SIGNAL ANALYZER measurement for noise analysis
        self.APx.AddMeasurement("Signal Path1", MeasurementType.SignalAnalyzer)
        self.APx.SignalAnalyzer.AcquisitionSeconds = 5.0
        self.APx.SignalAnalyzer.AcquisitionType = AcqLengthType.Seconds
        self.APx.SignalAnalyzer.Averages = 10
        self.APx.SignalAnalyzer.AnalogInputBandwidth = SignalAnalyzerBandwidthType.Bw20k44kHz

        # Add a derived result and configure it
        noise_result = self.APx.SignalAnalyzer.AmplitudeSpectralDensity.Result.AsXYGraph()
        noise_result.Name = "Voltage Noise Density"
        noise_result.Checked = True

    def run_noise_measurement(self):
        print("Starting voltage noise density measurement...")
        self.APx.Sequence.Run()
        # Wait for completion
        while self.APx.Sequence.IsRunning:
            print("Waiting for measurement to complete...")
            time.sleep(0.1)

        frequencies = list(self.APx.Sequence[0]["Signal Path1"].SequenceResults["Voltage Noise Density"].GetXValues(InputChannelIndex.Ch1, VerticalAxis.Left, SourceDataType.Measured, 1))
        noise_levels = list(self.APx.Sequence[0]["Signal Path1"].SequenceResults["Voltage Noise Density"].GetYValues(InputChannelIndex.Ch1, VerticalAxis.Left, SourceDataType.Measured, 1))

        cutoff = int(input("Enter cutoff frequency in Hz: "))
        filtered_freqs = [f for f in frequencies if f < cutoff]
        filtered_noise = [n for n, f in zip(noise_levels, frequencies) if f < cutoff]
        return filtered_freqs, filtered_noise


