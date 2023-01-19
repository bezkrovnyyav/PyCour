import socket


UDP_MAX_SIZE = 65535


def listen(host: str = '127.0.0.1', port: int = 3000):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    server_socket.bind((host, port))
    print(f'Listening at {host}:{port}')

    members = []
    while True:
        msg, addr = server_socket.recvfrom(UDP_MAX_SIZE)

        if addr not in members:
            members.append(addr)

        if not msg:
            continue

        client_id = addr[1]
        if msg.decode('ascii') == '__join':
            print(f'Client {client_id} joined chat')
            continue

        msg = f'client{client_id}: {msg.decode("ascii")}'
        for member in members:
            if member == addr:
                continue

            server_socket.sendto(msg.encode('ascii'), member)


if __name__ == '__main__':
    listen()
