package Q7;

import java.io.*;
import java.net.*;

public class ReliableClient {
    private static final String SERVER_ADDRESS = "localhost";
    private static final int SERVER_PORT = 9999;

    public static void main(String[] args) {
        try (Socket socket = new Socket(SERVER_ADDRESS, SERVER_PORT);
             BufferedReader in = new BufferedReader(new InputStreamReader(socket.getInputStream()));
             PrintWriter out = new PrintWriter(socket.getOutputStream(), true);
             BufferedReader consoleInput = new BufferedReader(new InputStreamReader(System.in))) {

            String input;
            System.out.println("Enter messages to send to the server (type 'exit' to quit):");
            while ((input = consoleInput.readLine()) != null) {
                // Send the message to the server
                out.println(input); 
                // Wait for acknowledgment
                String ack = in.readLine(); 
                // Print the acknowledgment received from the server
                System.out.println(ack); 

                // Break the loop if the user types 'exit'
                if ("exit".equalsIgnoreCase(input)) {
                    break;
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
