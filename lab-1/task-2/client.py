import socket 
from traits import port, ip

class Client:
    
    def __init__(self, port):
        self.port = port
        
        
    def start_client(self):
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        host = str(ip)[:len(str(ip))-1]
        print("Connecting to server: ", host)
        client_socket.connect((host, self.port))
        
        message_to_server = str(input("Enter message to send to server: "))
        client_socket.send(message_to_server.encode('ascii'))
        
        response = client_socket.recv(1024).decode('ascii')
        print(f"Response from server: {response}")
        client_socket.close()
        
        
        
if __name__ == "__main__":
    client = Client(port=port)
        
    client.start_client()