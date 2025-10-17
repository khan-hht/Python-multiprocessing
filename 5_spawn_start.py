import multiprocessing
import os
import time

global_variable = 20

def child_process():
    global global_variable
    print(f"Global Variable (Before) child process: {global_variable}")
    global_variable = 40
    print(f"Global Variable (After) child process: {global_variable}")
    time.sleep(1)
    print("Child process completed")

def parent_process():
    global global_variable
    print(f"Global Variable (Before) parent process: {global_variable}")
    global_variable = 30
    print(f"Global Variable (After) parent process: {global_variable}")

    process = multiprocessing.Process(target=child_process)
    process.start()
    process.join()

    print("Parent process completed")
    print(f"Global Variable (End) parent process: {global_variable}")


if __name__ == "__main__":
    print(multiprocessing.get_all_start_methods())
    print(multiprocessing.get_start_method())
    
    parent_process()

# For start method 'fork'
# The child process inherits the memory space of the parent process.
# Changes made to global_variable in the child process do not affect the parent process.
# In this case, in the child process at the beginning global_variable is 30 (inherited from parent),
# then it changes to 40, but the parent process remains unaffected with its own value of 30.
# For start method 'spawn'
# A new Python interpreter is started for the child process.   
# The child process does not inherit the memory space of the parent process.
# Changes made to global_variable in the child process do not affect the parent process.
# In this case, in the child process at the beginning global_variable is 20 (the original value),
# then it changes to 40, but the parent process remains unaffected with its own value of 30.
# For start method 'forkserver'
# A server process is started to manage the child processes.
# The child processes do not inherit the memory space of the parent process.
# Changes made to global_variable in the child process do not affect the parent process.   
# In this case, in the child process at the beginning global_variable is 20 (the original value),
# then it changes to 40, but the parent process remains unaffected with its own value of 30.
# Note: The actual behavior may vary based on the operating system and Python version.