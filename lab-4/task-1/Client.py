import socket

class Client:
    def __init__(self) -> None:
        pass
    
    def main(self):
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        server_address = ('localhost', 8080)
        print(f"Connecting to {server_address[0]} port {server_address[1]}")
        client_socket.connect(server_address)

        try:
            message = "This is a test message from the client.".encode('utf-8')
            print(f"Sending message: {message}")
            client_socket.sendall(message)

            data = client_socket.recv(1024)
            print(f"Received response from server: {data.decode('utf-8')}")

        finally:
            print("Closing client socket")
            client_socket.close()