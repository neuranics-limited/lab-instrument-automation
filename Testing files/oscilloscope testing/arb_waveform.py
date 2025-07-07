# Example: 1 cycle of a triangle wave, normalized to -1 to 1, 1000 points
import numpy as np

points = 1000
# Triangle wave: ramp up from -1 to 1, then down from 1 to -1
half = points // 2
triangle = np.concatenate([
    np.linspace(-1, 1, half, endpoint=False),
    np.linspace(1, -1, points - half)
])

np.savetxt('arb_waveform.csv', triangle, delimiter=',')
