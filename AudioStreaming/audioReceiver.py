import socket
import pyaudio

CHUNK = 4096
FORMAT = pyaudio.paInt8
CHANNELS = 1
RATE = 20480
MY_ADDR = ("localhost", 5000)
OTHER_ADDR = ("localhost", 5001)
#MY_ADDR = ("", 5000)
#OTHER_ADDR = ("192.168.1.144", 5000)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(MY_ADDR)

p = pyaudio.PyAudio()
stream = p.open(format=FORMAT, channels=1, rate=RATE, output=True)

print("audio player started")
data, addr = sock.recvfrom(CHUNK)
while data != '':
    stream.write(data)
    data, addr = sock.recvfrom(CHUNK)

stream.stop_stream()
stream.close()
p.terminate()