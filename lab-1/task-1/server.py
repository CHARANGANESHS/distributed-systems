import socket
from traits import port

class Server:
    
    def __init__(self, port):
        self.port = port
        
    def start_server(self):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        host = socket.gethostname()
        server_socket.bind((host, self.port))
        server_socket.listen(5)
        print("Server is listening on port: ", self.port)
        
        while True:
            client_socket, addr = server_socket.accept()
            print("Got connection from: ", addr)
            message = "Thank you for connecting to the server\n"
            client_socket.send(message.encode('ascii'))
            client_socket.close()
    
    
if __name__ == "__main__":
    server = Server(port=port)
    server.start_server()