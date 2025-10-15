from time import sleep
from multiprocessing import Process

def task():
    print("Task started")
    sleep(5)
    print("Task completed")

if __name__ == "__main__":
    process = Process(target=task) # Create a new process
    process.start() # Start the process
    process.join() # Wait for the process to finish
    print("Process finished")