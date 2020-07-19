from scipy import signal
from scipy.fft import fft, fftshift
import matplotlib.pyplot as plt
import numpy as np
fig, (ax1,ax2) = plt.subplots(2)
window = signal.gaussian(51, std=7)
ax1.plot(window)
ax1.set_title(r"Gaussian window ($\sigma$=7)")
ax1.set_ylabel("Amplitude")
ax1.set_xlabel("Sample")
A = fft(window, 2048) / (len(window)/2.0)
freq = np.linspace(-0.5, 0.5, len(A))
response = 20 * np.log10(np.abs(fftshift(A / abs(A).max())))
ax2.plot(freq, response)
plt.axis([-0.5, 0.5, -120, 0])
ax2.set_title(r"Frequency response of the Gaussian window ($\sigma$=7)")
ax2.set_ylabel("Normalized magnitude [dB]")
ax2.set_xlabel("Normalized frequency [cycles per sample]")
plt.show()