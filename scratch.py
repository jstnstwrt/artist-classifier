import sys
import numpy as np
from scipy.io import wavfile
from scipy import signal
from matplotlib import pyplot as plt

WAVE_FILE_PATH = './samples/whistle.wav'
MAX_LENGTH = 10;

if len(sys.argv) > 1:
    wave_file = sys.argv[1]
else:
    wave_file = WAVE_FILE_PATH

[fs, audio_in] = wavfile.read(wave_file)
print "fs: %i kHz" % fs

# Only use one channel
if np.matrix(audio_in).shape[1] > 1:
    audio_in = audio_in[:,0]

if len(audio_in) > MAX_LENGTH * fs:
    audio_in = audio_in[0:MAX_LENGTH * fs]


f, t, Sxx = signal.spectrogram(audio_in, fs, nperseg=100)
plt.pcolormesh(t, f, Sxx)
plt.ylabel('Frequency [Hz]')
plt.xlabel('Time [sec]')
plt.show()

exit()


