import clr

# Add a reference to the APx API
clr.AddReference(r"C:\Program Files\Audio Precision\APx500 9.1\API\AudioPrecision.API3.dll")        
clr.AddReference(r"C:\Program Files\Audio Precision\APx500 9.1\API\AudioPrecision.API2.dll")    
clr.AddReference(r"C:\Program Files\Audio Precision\APx500 9.1\API\AudioPrecision.API.dll") 
from AudioPrecision.API import *

# Instantiate and create a new project
APx = APx500_Application()
APx.Visible = True
APx.CreateNewProject()

# Set to bench mode (no measurement setup needed)
APx.SignalPathSetup.OutputConnector.Type = OutputConnectorType.AnalogUnbalanced  # or AnalogBalanced

# Configure the generator for sine wave output
APx.Generator.Type = GeneratorType.SineWave
APx.Generator.Frequency.Value = 1000  # 1 kHz
APx.Generator.Levels.SetValue(OutputChannelIndex.Ch1, "1 Vrms")  # 1 Vrms output level

# Enable the generator output
APx.Generator.OutputEnabled = True

print("APx555 is now in bench mode outputting a 1 kHz sine wave at 1 Vrms on Analog Output 1")
print("Press Enter to stop the output...")
input()

# Disable output when done
APx.Generator.OutputEnabled = False
print("Output disabled.")