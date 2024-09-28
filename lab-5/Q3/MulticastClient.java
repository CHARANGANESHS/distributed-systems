package Q3;

import java.net.*;
import java.nio.charset.StandardCharsets;
import java.util.Scanner;

public class MulticastClient {
    private static int clientCount = 0;

    public static void main(String[] args) {
        String groupAddress = "224.0.0.1"; // Multicast group address
        int port = 9999;

        // Each client gets a unique client number
        @SuppressWarnings("unused")
        int clientNumber = clientCount++;

        try (MulticastSocket socket = new MulticastSocket(port)) {
            InetAddress group = InetAddress.getByName(groupAddress);

            // Find and use the first available network interface for multicast
            NetworkInterface networkInterface = NetworkInterface.getByInetAddress(InetAddress.getLocalHost());
            if (networkInterface == null) {
                System.out.println("No suitable network interface found.");
                return;
            }

            // Join the multicast group using the network interface
            socket.joinGroup(new InetSocketAddress(group, port), networkInterface);

            // Thread to receive messages
            new Thread(() -> {
                byte[] buffer = new byte[1024];
                DatagramPacket packet = new DatagramPacket(buffer, buffer.length);

                while (true) {
                    try {
                        socket.receive(packet);
                        String receivedMessage = new String(packet.getData(), 0, packet.getLength());
                        System.out.println("Received: \"" + receivedMessage + "\""); // Show the received message in the required format
                    } catch (Exception e) {
                        e.printStackTrace();
                    }
                }
            }).start();

            // Send messages entered by the user
            @SuppressWarnings("resource")
            Scanner scanner = new Scanner(System.in);
            while (true) {
                String message = scanner.nextLine();

                // Append client number to the message
                String messageToSend = "Client : " + message;
                byte[] buffer = messageToSend.getBytes(StandardCharsets.UTF_8);
                DatagramPacket packet = new DatagramPacket(buffer, buffer.length, group, port);

                socket.send(packet);
                System.out.println("Sent to \"" + messageToSend + "\""); // Show the sent message in the required format
            }

        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
