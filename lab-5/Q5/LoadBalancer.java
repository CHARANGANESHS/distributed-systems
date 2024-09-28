package Q5;

import java.util.concurrent.BlockingQueue;
import java.util.concurrent.LinkedBlockingQueue;

public class LoadBalancer {
    private BlockingQueue<String> taskQueue;
    private static LoadBalancer instance;

    // Singleton instance to ensure only one load balancer
    private LoadBalancer() {
        taskQueue = new LinkedBlockingQueue<>();

        // Create and start "worker" threads to process tasks
        for (int i = 1; i <= 5; i++) {  
            int workerId = i;
            new Thread(() -> processTasks(workerId)).start();
        }
    }

    public static synchronized LoadBalancer getInstance() {
        if (instance == null) {
            instance = new LoadBalancer();
        }
        return instance;
    }

    // Add a new task to the queue
    public void addTask(String task) {
        try {
            taskQueue.put(task);  // Blocking call, waits if the queue is full
            System.out.println("\nTask added to LoadBalancer: " + task + "\n");
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }

    // Process tasks assigned to each "worker" thread
    private void processTasks(int workerId) {
        while (true) {
            try {
                // Take the next task from the queue (blocks if no tasks are available)
                String task = taskQueue.take();
                System.out.println("\nWorker " + workerId + " processing task: " + task + "\n");
                // Simulate task processing time
                Thread.sleep(4000);  // Simulate time taken to process the task
                System.out.println("\nWorker " + workerId + " completed task: " + task + "\n");

            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }
}
