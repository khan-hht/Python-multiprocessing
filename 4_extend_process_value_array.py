from time import sleep
from multiprocessing import Process, Value, Array as Valuearray

class CustomProcess(Process):
    def __init__(self):
        super().__init__()  # Initialize the base Process class
        self.data = Value('i', 1)  # Shared integer value
        self.array = Valuearray('i', range(5))  # Shared array of integers
    
    def run(self):
        print("Process started")
        print(f"Initial data value: {self.data.value}")
        print(f"Initial array values: {list(self.array)}")
        sleep(5)
        print("Process completed")


if __name__ == "__main__":
    process = CustomProcess()  # Create an instance of CustomProcess
    process.start()  # Start the process
    process.join()  # Wait for the process to finish
    print("Process finished")
    print(f"From parent data value: {process.data.value}")
    print(f"From parent array values: {list(process.array)}")
