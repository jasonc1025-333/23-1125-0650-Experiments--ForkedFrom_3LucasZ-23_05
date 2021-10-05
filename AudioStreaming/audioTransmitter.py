import socket
import pyaudio

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 10240
MY_ADDR = ("", 5000)
OTHER_ADDR = ("localhost", 5000)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

p = pyaudio.PyAudio()
stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)

print("recording started")
while True:
    data = stream.read(CHUNK)
    sock.sendto(data, OTHER_ADDR)

stream.stop_stream()
stream.close()
p.terminate()