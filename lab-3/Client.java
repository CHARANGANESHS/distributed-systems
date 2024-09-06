import java.io.*;
import java.net.*;

public class Client {
    public static void main(String[] args) {
        String serverIp = "10.70.38.115"; 
        int port = 12345;

        try (Socket socket = new Socket(serverIp, port)) {
            System.out.println("Connected to the server");

            OutputStream output = socket.getOutputStream();
            PrintWriter writer = new PrintWriter(output, true);

            InputStream input = socket.getInputStream();
            BufferedReader reader = new BufferedReader(new InputStreamReader(input));

            String message;
            while (true) {
                BufferedReader clientInput = new BufferedReader(new InputStreamReader(System.in));
                System.out.print("Client: ");
                message = clientInput.readLine();
                writer.println(message);

                if (message.equalsIgnoreCase("exit") || message.equalsIgnoreCase("quit")) {
                    System.out.println("Client disconnected");
                    socket.close();
                    break;
                }

                String serverResponse = reader.readLine();
                System.out.println(serverResponse);
            }

        } catch (UnknownHostException ex) {
            System.out.println("Server not found: " + ex.getMessage());
        } catch (IOException ex) {
            System.out.println("I/O error: " + ex.getMessage());
        }
    }
}