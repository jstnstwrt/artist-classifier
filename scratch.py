import numpy as np
from scipy.io import wavfile
from scipy import signal
from matplotlib import pyplot as plt

WAVE_FILE_PATH = './samples/whistle.wav'

[fs, audio_in] = wavfile.read(WAVE_FILE_PATH)
print "fs: %i kHz" % fs

audio_in = audio_in[:,0]

f, t, Sxx = signal.spectrogram(audio_in, fs, nperseg=1000)
plt.pcolormesh(t, f, Sxx)
plt.ylabel('Frequency [Hz]')
plt.xlabel('Time [sec]')
plt.show()

exit()


