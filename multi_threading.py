import threading
import time


class MyThread(threading.Thread):
    def __init__(self, name, delay, counter):
        super().__init__()
        self.name = name
        self.delay = delay
        self.counter = counter

    def run(self) -> None:
        print(f"Starting thread {self.name}")
        print_thread(self.name, self.delay, self.counter)
        print(f"Ending thread {self.name}")


class SynchronizedThread(threading.Thread):
    lock = threading.Lock()  # Variables declared inside the class definition, but not inside a method are class or
    # static variables

    def __init__(self, name, delay, counter):
        super().__init__()
        self.name = name
        self.delay = delay
        self.counter = counter

    def run(self) -> None:
        print(f"Starting thread {self.name}")
        self.lock.acquire()
        print_thread(self.name, self.delay, self.counter)
        print(f"Ending thread {self.name}")
        self.lock.release()


def print_thread(thread_name, delay, counter):
    count = 0
    while count < counter:
        time.sleep(delay)
        print(thread_name, time.ctime(time.time()))
        count += 1


# thread1 = MyThread("Thread01", 5, 3)
# thread2 = MyThread("Thread02", 3, 5)

thread1 = SynchronizedThread("Thread01", 5, 3)
thread2 = SynchronizedThread("Thread02", 3, 5)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("Exiting main thread")
