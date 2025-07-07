import matplotlib.pyplot as plt
import numpy as np
import os
import re

# Path to the CSV file (same directory as this script)
csv_file = os.path.join(os.path.dirname(__file__), 'oscilloscope_capture.csv')

# Read the CSV data (assuming ASCII, comma-separated values)
with open(csv_file, 'r') as f:
    data = f.read()

# Remove header if present (e.g., #513999)
header_match = re.match(r'#(\\d)(\\d+)', data)
if data.startswith('#'):
    # Find the header length
    header_len_digits = int(data[1])
    header_len = 2 + header_len_digits  # '#' + digit + N digits
    data_start = header_len + int(data[2:2+header_len_digits])
    # Remove header
    data = data[header_len:]

# Now parse the data
y = np.array([float(val) for val in data.replace('\n', ',').split(',') if val.strip() and not val.strip().startswith('#')])

# Generate a sample x-axis (since only y-data is saved)
x = np.arange(len(y))

plt.figure(figsize=(10, 4))
plt.plot(x, y, label='Oscilloscope waveform')
plt.xlabel('Sample Index')
plt.ylabel('Voltage (V)')
plt.title('Oscilloscope Waveform from CSV')
plt.legend()
plt.tight_layout()
plt.show()