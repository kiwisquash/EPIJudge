import threading
import time

CAP = 100

output_list = []
dt = 1

def print_odds():
    for i in range(1,CAP,2):
        print(i)
        output_list.append(i)
        time.sleep(dt)

def print_evens():
    for i in range(2,CAP+1,2):
        print(i)
        output_list.append(i)
        time.sleep(dt)

if __name__ == "__main__":
    t1 = threading.Thread(target=print_odds)
    t2 = threading.Thread(target=print_evens)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Complete!")
    print(f"See this list {output_list}")
    print(output_list == list(range(1,101)))

