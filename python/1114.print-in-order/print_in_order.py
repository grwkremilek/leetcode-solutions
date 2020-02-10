#https://leetcode.com/problems/print-in-order/

# locks
class Foo:
    def __init__(self):       
        self.lock1 = threading.Lock()
        self.lock2 = threading.Lock()
        
        self.lock1.acquire()            # locked (second thread is waiting)
        self.lock2.acquire()            # locked (third thread is waiting)

    def first(self, printFirst: 'Callable[[], None]') -> None:
        printFirst()
        self.lock1.release()            # first thread unlocks lock1, second thread can procede with def second

    def second(self, printSecond: 'Callable[[], None]') -> None:
        self.lock1.acquire()            # locked (wait for first funtion to finish)
        printSecond()
        self.lock2.release()            # second thread unlocks lock2, third thread can procede with def third

    def third(self, printThird: 'Callable[[], None]') -> None:
        self.lock2.acquire()            # locked (wait for second funtion to finish)
        printThird()



#semaphores
class Foo:
    def __init__(self):       
        self.gate1 = threading.Semaphore(0)
        self.gate2 = threading.Semaphore(0)
        
    def first(self, printFirst: 'Callable[[], None]') -> None:
        printFirst()
        self.gate1.release()
        
    def second(self, printSecond: 'Callable[[], None]') -> None:
        with self.gate1:
            printSecond()
        self.gate2.release()

    def third(self, printThird: 'Callable[[], None]') -> None:
        with self.gate2:
            printThird()


#events
class Foo:
    def __init__(self):       
        self.event1 = threading.Event()
        self.event2 = threading.Event()
        

    def first(self, printFirst: 'Callable[[], None]') -> None:
        printFirst()
        self.event1.set()
        
    def second(self, printSecond: 'Callable[[], None]') -> None:
        self.event1.wait()
        printSecond()
        self.event2.set()

    def third(self, printThird: 'Callable[[], None]') -> None:
        self.event2.wait()
        printThird()
