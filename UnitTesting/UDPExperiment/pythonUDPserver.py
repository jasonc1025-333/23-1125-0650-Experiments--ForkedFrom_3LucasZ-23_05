import time
import socket
import threading
import time

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('localhost', 5000))
client = ('localhost',2000)

def sender():
    global client
    print('Sender thread started')
    data = bytes([0x98 for x in range(100)])
    while True:
        server_socket.sendto(data, client)
        print("Sent:", data)
        time.sleep(1)

def receiver():
    global client
    print('Receiver thread started')
    while True:
        data, client = server_socket.recvfrom(1)
        print("Received:", data)
        time.sleep(1)

if __name__ == "__main__":
    sender_thread = threading.Thread(target=sender)
    receiver_thread = threading.Thread(target=receiver)
    sender_thread.start()
    receiver_thread.start()