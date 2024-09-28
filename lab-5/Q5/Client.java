package Q5;

import java.util.Scanner;
import Q5.LoadBalancer;

@SuppressWarnings("unused")
public class Client {
    public static void main(String[] args) {
        LoadBalancer loadBalancer = LoadBalancer.getInstance(); 

        @SuppressWarnings("resource")
        Scanner scanner = new Scanner(System.in);
        while (true) {
            System.out.print("Enter task to send to LoadBalancer: ");
            String task = scanner.nextLine();

            loadBalancer.addTask(task); 
        }
    }
}
