import numpy as np

amostra = np.array([12, 23, 43, 3, 8, 20, 9])

amplitude = amostra.max() - amostra.min()

print('Amplitude: %s', amplitude)
#amplitude: 40