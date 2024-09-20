from CounterIncrement import CounterIncrementer

if __name__ == '__main__':
    counter_incrementer = CounterIncrementer(number_of_processes=3)
    counter_incrementer.run_processes(num_increments_per_process=10)
