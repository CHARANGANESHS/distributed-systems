import multiprocessing
import time


class CounterIncrementer:
    def __init__(self, number_of_processes=6, initial_value=0):
        self.counter = multiprocessing.Value('i', initial_value)
        self.lock = multiprocessing.Lock()
        self.number_of_processes = number_of_processes

    def increment_counter(self, num_increments, process_name):
        for _ in range(num_increments):
            with self.lock:
                self.counter.value += 1
                print(f"{process_name} incremented counter to {self.counter.value}")
            time.sleep(0.3)

    def run_processes(self, num_increments_per_process=10):
        
        processes = []
        
        for i in range(self.number_of_processes):
            process = multiprocessing.Process(target=self.increment_counter, args=(num_increments_per_process, f"Process {i}"))
            processes.append(process)
            
        for i in range(self.number_of_processes):
            processes[i].start()
            
        for i in range(self.number_of_processes):
            processes[i].join() 
            
        print(f"Final counter value: {self.counter.value}")
