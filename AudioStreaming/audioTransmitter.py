import socket
import pyaudio

CHUNK = 4096
FORMAT = pyaudio.paInt8
CHANNELS = 1
RATE = 20480
#MY_ADDR = ("localhost", 5001)
#OTHER_ADDR = ("localhost", 5000)
MY_ADDR = ("192.168.1.144", 5001)
OTHER_ADDR = ("192.168.1.139", 5001)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

p = pyaudio.PyAudio()
stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)

print("recording started")
while True:
    data = stream.read(CHUNK)
    print(len(data))
    sock.sendto(data, OTHER_ADDR)

stream.stop_stream()
stream.close()
p.terminate()