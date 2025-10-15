from time import sleep
from multiprocessing import Process


def task(sleep_time, task_name):
    print(f"{task_name} started")
    sleep(sleep_time)
    print(f"{task_name} completed")


if __name__ == "__main__":
    sleep_time, task_name = input("Enter the sleep time and task name : ").split()
    sleep_time = int(sleep_time)
    process = Process(target=task, args=(sleep_time, task_name)) # Create a new process with arguments
    process.start() # Start the process
    process.join() # Wait for the process to finish
    print("Process finished")