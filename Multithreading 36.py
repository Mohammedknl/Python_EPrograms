import threading
import time
def task1():
    print("Task 1 started")
    time.sleep(2) # simulate a time-consuming task
    print("Task 1 completed")
def task2():
    print("Task 2 started")
    time.sleep(1) # simulate a time-consuming task
    print("Task 2 completed")
def main():
    # create two threads, one for each task
    t1 = threading.Thread(target=task1)
    t2 = threading.Thread(target=task2)
    # start the threads
    t1.start()
    t2.start()
    # wait for the threads to complete
    t1.join()
    t2.join()
    # print a message indicating that the program has completed
    print("Program completed")
if __name__ == '__main__':
    main()
