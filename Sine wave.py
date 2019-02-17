import numpy as np
import wave
import struct
import matplotlib.pyplot as plt

frequency= 440
num_samples=48000
samplingr=48000.0
amplitude= 16000
file= "test.wav"

sine_wave=[np.sin(2*np.pi*frequency*x/samplingr) for x in range(num_samples)]
print(sine_wave)
nframes=num_samples
comptype="NONE"
compname="not compressed"
nchannels=1
sampwidth=2

wav_file=wave.open(file, "w")
wav_file.setparams((nchannels, sampwidth, int(samplingr), nframes, comptype, compname))

for s in sine_wave:
                 wav_file.writeframes(struct.pack('h', int(s*amplitude)))

