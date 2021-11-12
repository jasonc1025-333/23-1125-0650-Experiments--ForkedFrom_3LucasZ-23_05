import socket
import pyaudio
import threading

CHUNK = 4096
FORMAT = pyaudio.paInt8
CHANNELS = 1
RATE = 20480

MY_ADDR = ("", 7000)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(MY_ADDR)

p = pyaudio.PyAudio()
stream = p.open(format=FORMAT, channels=1, rate=RATE, output=True)

data = 'empty'
def receive_thread():
    global data
    while data!= '':
        print("Received.")
        data, addr = sock.recvfrom(CHUNK)

def play_thread():
    global data
    print("audio player started")
    while data == 'empty':
        pass
    while data != '':
        stream.write(data)

if __name__ == "__main__":
    # creating thread
    t1 = threading.Thread(target=receive_thread)
    t2 = threading.Thread(target=play_thread)
  
    # starting thread 1
    t1.start()
    # starting thread 2
    t2.start()

#cleanup
#stream.stop_stream()
#stream.close()
#p.terminate()