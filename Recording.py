import pyaudio
import struct
import numpy as np
import matplotlib.pyplot as plt

#Chunk =samples to be recorded on a single run
#Channels= Mono
#Recording duartion= Chunk/SampleRate
Chunk =  48000
Format = pyaudio.paInt16
CHANNELS = 1
Rate = 48000

#creating a class
p = pyaudio.PyAudio()
stream = p.open(
    format=Format,
    channels= CHANNELS,
    rate=Rate,
    input=True,
    output=True,
    frames_per_buffer=Chunk
)

data = stream.read(Chunk)

data= struct.unpack(str(2* Chunk) + 'b', data)


DataArray = np.array(data)

data_fft= np.fft.fft(DataArray)

frequencies=np.abs(data_fft)

filtered_freq = []

filtered_freq = [f if (50< index <2000 and f > 1) else 0 for index, f in enumerate(frequencies)]


print("the frequency is {} Hz".format(np.argmax(filtered_freq)))

plt.subplot(2, 1, 1)
plt.plot(filtered_freq)
plt.xlim(50, 2000)
plt.show()

plt.close()




