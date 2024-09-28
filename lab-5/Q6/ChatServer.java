package Q6;

import java.io.*;
import java.net.*;
import java.util.*;
import java.util.concurrent.*;

public class ChatServer {
    private static final int PORT = 9999;
    private static Map<String, CopyOnWriteArrayList<ClientHandler>> chatRooms = new ConcurrentHashMap<>();

    public static void main(String[] args) {
        System.out.println("Chat server started...");
        try (ServerSocket serverSocket = new ServerSocket(PORT)) {
            while (true) {
                Socket clientSocket = serverSocket.accept();
                new Thread(new ClientHandler(clientSocket)).start();
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    static class ClientHandler implements Runnable {
        private Socket socket;
        private String username;
        private String currentRoom;
        private PrintWriter out;
        private BufferedReader in;

        public ClientHandler(Socket socket) {
            this.socket = socket;
        }

        @Override
        public void run() {
            try {
                in = new BufferedReader(new InputStreamReader(socket.getInputStream()));
                out = new PrintWriter(socket.getOutputStream(), true);

                // Get the username
                out.println("Enter your username:");
                username = in.readLine();
                out.println("Welcome, " + username + "!");

                while (true) {
                    out.println("Available commands: \n/join <room>\n/send <message>\n/exit");
                    String input = in.readLine();
                    if (input.startsWith("/join")) {
                        joinRoom(input.split(" ")[1]);
                    } else if (input.startsWith("/send")) {
                        sendMessage(input.substring(6));
                    } else if (input.equalsIgnoreCase("/exit")) {
                        exitRoom();
                        break;
                    }
                }
            } catch (IOException e) {
                e.printStackTrace();
            } finally {
                try {
                    socket.close();
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
        }

        private void joinRoom(String roomName) {
            if (currentRoom != null) {
                chatRooms.get(currentRoom).remove(this);
            }

            currentRoom = roomName;
            chatRooms.putIfAbsent(roomName, new CopyOnWriteArrayList<>());
            chatRooms.get(roomName).add(this);

            // Log on server when user joins a room
            System.out.println("User " + username + " joined room " + roomName);

            out.println("Joined chat room: " + roomName);
            broadcastMessage("User " + username + " has joined the room.");
        }

        private void sendMessage(String message) {
            if (currentRoom == null) {
                out.println("You must join a room first!");
                return;
            }
            broadcastMessage(username + ": " + message);
        }

        private void broadcastMessage(String message) {
            for (ClientHandler client : chatRooms.get(currentRoom)) {
                client.out.println(message);
            }
        }

        private void exitRoom() {
            if (currentRoom != null) {
                chatRooms.get(currentRoom).remove(this);
                broadcastMessage("User " + username + " has left the room.");
            }
        }
    }
}
