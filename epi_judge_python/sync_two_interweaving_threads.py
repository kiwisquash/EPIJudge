import threading
import time

CAP = 100

output_list = []
dt = .1

def print_odds():
    for i in range(1,CAP,2):
        with lock:
            while (output_list and output_list[-1] % 2 == 1): 
                time.sleep(dt)
            print(i)
            output_list.append(i)

def print_evens():
    print('KS')
    print(output_list)
    for i in range(2,CAP+1,2):
        with lock:
            while (output_list and output_list[-1] % 2 == 0): 
                time.sleep(dt)
            output_list.append(i)
            time.sleep(dt)

if __name__ == "__main__":
    lock = threading.Lock()
    t1 = threading.Thread(target=print_odds)
    t2 = threading.Thread(target=print_evens)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Complete!")
    print(f"See this list {output_list}")
    print(output_list == list(range(1,101)))

