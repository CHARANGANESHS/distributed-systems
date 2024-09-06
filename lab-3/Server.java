import java.io.*;
import java.net.*;

public class Server {
    public static void main(String[] args) {
        int port = 12345;
        try (ServerSocket serverSocket = new ServerSocket(port)) {
            System.out.println("Server is listening on port " + port);

            while (true) {
                Socket socket = serverSocket.accept();
                InetAddress clientAddress = socket.getInetAddress();
                System.out.println("New client connected: " + clientAddress.getHostAddress());

                new ClientHandler(socket).start();
            }

        } catch (IOException ex) {
            System.out.println("Server exception: " + ex.getMessage());
            ex.printStackTrace();
        }
    }
}

class ClientHandler extends Thread {
    private Socket socket;

    public ClientHandler(Socket socket) {
        this.socket = socket;
    }

    public void run() {
        try {
            InputStream input = socket.getInputStream();
            BufferedReader reader = new BufferedReader(new InputStreamReader(input));

            OutputStream output = socket.getOutputStream();
            PrintWriter writer = new PrintWriter(output, true);

            InetAddress clientAddress = socket.getInetAddress();
            System.out.println("Client IP: " + clientAddress.getHostAddress());

            String clientMessage;
            while ((clientMessage = reader.readLine()) != null) {
                System.out.println("Client (" + clientAddress.getHostAddress() + "): " + clientMessage);
                
                String reverse_msg = new StringBuilder(clientMessage).reverse().toString();
                writer.println("Server (reversed): " + reverse_msg);

                if (clientMessage.equalsIgnoreCase("exit") || clientMessage.equalsIgnoreCase("quit")) {
                    System.out.println("Client disconnected.");
                    socket.close();
                    break;
                }
            }

        } catch (IOException ex) {
            System.out.println("Server exception: " + ex.getMessage());
            ex.printStackTrace();
        }
    }
}