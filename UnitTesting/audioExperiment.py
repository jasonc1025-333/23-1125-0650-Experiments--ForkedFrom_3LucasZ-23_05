import pyaudio

p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16,  channels=1, rate=10000, input=False, output=True)

data = bytes([0x99 for x in range(10000)])
while data != '':
    stream.write(data)
    data = bytes([0x99 for x in range(10000)])
    
stream.stop_stream()
stream.close()
p.terminate()