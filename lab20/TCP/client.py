import time
import socket


HOST = "127.0.0.1"
PORT = 65432

if __name__ == "__main__":

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((HOST, PORT))

        with open('client_picture.jpg', 'rb') as img:
            start_time = time.time()
            img_data = img.read(1024)

            while img_data:
                client_socket.send(img_data)
                img_data = img.read(1024)

            end_time = time.time()
            finish_time = end_time - start_time
            print(f"Picture sent in {finish_time} seconds")
