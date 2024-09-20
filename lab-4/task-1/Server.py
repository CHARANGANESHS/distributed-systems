import socket
import struct

class Server:

    def __init__(self) -> None:
        pass

    def main(self):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_address = ('localhost', 8080)
        server_socket.bind(server_address)
        server_socket.listen(1)
        
        print("Server is running. Waiting for a client to connect...")

        connection, client_address = server_socket.accept()

        try:
            print(f"Connection from {client_address}")
            
            connection.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)
            print("SO_KEEPALIVE enabled: ", connection.getsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE))
            
            connection.setsockopt(socket.SOL_SOCKET, socket.SO_LINGER, struct.pack('ii', 1, 30))
            print("SO_LINGER set to 30 seconds.")
            
            connection.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, 8192)
            connection.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, 8192)
            print("SO_SNDBUF: ", connection.getsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF))
            print("SO_RCVBUF: ", connection.getsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF))
            
            connection.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
            print("TCP_NODELAY enabled: ", connection.getsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY))
            
            data = connection.recv(1024)
            print(f"Received: {data.decode('utf-8')}")
            
            response = "Message received".encode('utf-8')
            connection.sendall(response)

        finally:
            print("Closing connection")
            connection.close()
