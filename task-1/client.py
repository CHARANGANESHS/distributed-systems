import socket 
from traits import port, ip

class Client:
    
    def __init__(self, port):
        self.port = port
        
        
    def start_client(self):
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        host = socket.gethostname()
        print("Connecting to server: ", host)
        client_socket.connect((host, self.port))
        
        message = client_socket.recv(1024).decode('ascii')
        client_socket.close()
        
        message.decode('ascii')
        
        
if __name__ == "__main__":
    client = Client(port=port)
        
    client.start_client()