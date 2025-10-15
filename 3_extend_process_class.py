from time import sleep
from multiprocessing import Process


class CustomProcess(Process):
    def __init__(self, sleep_time, task_name):
        super().__init__()  # Initialize the base Process class
        self.sleep_time = sleep_time
        self.task_name = task_name

    def run(self):
        print(f"{self.task_name} started")
        sleep(self.sleep_time)
        print(f"{self.task_name} completed")

if __name__ == "__main__":
    sleep_time, task_name = input("Enter the sleep time and task name : ").split()
    sleep_time = int(sleep_time)
    process = CustomProcess(sleep_time, task_name)  # Create an instance of CustomProcess
    process.start()  # Start the process
    process.join()  # Wait for the process to finish
    print("Process finished")
