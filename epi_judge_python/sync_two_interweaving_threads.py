import threading

CAP = 100

class OddEvenMonitor(threading.Condition):
    EVEN = False
    ODD = True

    def __init__(self):
        super().__init__()
        self.turn = self.ODD
    
    def wait_turn(self, old):
        with self:
            while self.turn != old:
                self.wait()

    def toggle_turn(self):
        with self:
            self.turn ^= True 
            self.notify()

class EvenThread(threading.Thread):

    def __init__(self, monitor):
        super().__init__()
        self.monitor = monitor

    def run(self): #Overwrites the run method
        for i in range(2,CAP+1,2):
            self.monitor.wait_turn(OddEvenMonitor.EVEN)
            print(i)
            self.monitor.toggle_turn()

class OddThread(threading.Thread):

    def __init__(self, monitor):
        super().__init__()
        self.monitor = monitor

    def run(self): #Overwrites the run method
        for i in range(1,CAP,2):
            self.monitor.wait_turn(OddEvenMonitor.ODD)
            print(i)
            self.monitor.toggle_turn()

if __name__ == "__main__":

    monitor = OddEvenMonitor()
    oddThread = OddThread(monitor)
    evenThread = EvenThread(monitor)

    oddThread.start()
    evenThread.start()
