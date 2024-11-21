import time
from multiprocessing import Queue, Process

def writer(queue):

    msgs = ["Message1", "Message2", "Terminating"]

    for msg in msgs:
        queue.put(msg)
        print(f"Message -- {msg} -- added to the Queue.")
        time.sleep(1)

def reader(queue):
    while True:
        time.sleep(1)
        msg = queue.get()
        if msg.lower() == "terminating":
            print("Termination Signal Received")
            print("Client Closing!")
            break
        print(f"Message Read from Queue-- {msg}.")

if __name__ == "__main__":

    queue = Queue()

    p1 = Process(target = writer, args = (queue,))
    p2 = Process(target = reader, args = (queue, ))

    p1.start()
    p2.start()

    p1.join()
    p2.join()