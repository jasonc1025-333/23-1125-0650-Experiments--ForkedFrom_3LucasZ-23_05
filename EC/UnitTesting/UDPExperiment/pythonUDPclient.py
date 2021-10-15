import time
import socket
import threading
import time


client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
addr = ("localhost", 5000)

def sender():
    print('Sender thread started')
    data = b'test'
    while True:
        client_socket.sendto(data, addr)
        print("Sent:", data)
        time.sleep(1)

def receiver():
    print('Receiver thread started')
    while True:
        data, server = client_socket.recvfrom(1)
        print("Received:", data)
        time.sleep(1)

if __name__ == "__main__":
    sender_thread = threading.Thread(target=sender)
    receiver_thread = threading.Thread(target=receiver)
    sender_thread.start()
    receiver_thread.start()
        