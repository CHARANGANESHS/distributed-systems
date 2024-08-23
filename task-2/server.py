import socket
from traits import port

class Server:
    
    def __init__(self, port):
        self.port = port
        
    def start_server(self):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        host = '0.0.0.0'
        server_socket.bind((host, self.port))
        server_socket.listen(5)
        print("Server is listening on port: ", self.port)
        
        while True:
            client_socket, addr = server_socket.accept()
            print("Got connection from: ", addr)
            
            message_from_client = client_socket.recv(1024).decode('ascii')
            print(f"Message from client: {message_from_client}")
            
            message = str(input("Enter message to send to client: "))
        
            client_socket.send(message.encode('ascii'))
            client_socket.close()
    
    
if __name__ == "__main__":
    server = Server(port=port)
    server.start_server()