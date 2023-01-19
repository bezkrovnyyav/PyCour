import socket
import threading
import os


UDP_MAX_SIZE = 65535


def listen(client_socket: socket.socket):
    while True:
        msg = client_socket.recv(UDP_MAX_SIZE)
        print('\r\r' + msg.decode('ascii') + '\n' + "You: ", end='')


def connect(host: str = '127.0.0.1', port: int = 3000):
    clint_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    clint_socket.connect((host, port))

    threading.Thread(target=listen, args=(clint_socket,), daemon=True).start()

    clint_socket.send('__join'.encode('ascii'))

    while True:
        msg = input("You: ")
        clint_socket.send(msg.encode('ascii'))


if __name__ == '__main__':
    os.system('clear')
    print('Welcome to chat!')
    connect()
