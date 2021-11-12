import socket
import pyaudio

CHUNK = 4096
FORMAT = pyaudio.paInt8
CHANNELS = 1
RATE = 20480

OTHER_ADDR = ("192.168.50.1", 7000)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

p = pyaudio.PyAudio()
stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)

print("recording started")
while True:
    data = stream.read(CHUNK)
    print(len(data))
    print(data)
    sock.sendto(data, OTHER_ADDR)

stream.stop_stream()
stream.close()
p.terminate()