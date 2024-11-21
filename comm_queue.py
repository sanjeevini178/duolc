import time
from multiprocessing import Process, Queue

def sender(queue):
    msg_list = ["Message 1", "Message 2", "Message 3", "Terminating"]

    for msg in msg_list:
        queue.put(msg)
        print(f"Sender sent -- {msg} -- to the queue.")
        time.sleep(1)

def reader(queue):
    while True:
        msg = queue.get()
        if msg == "Terminating":
            print("Termination signal Received.")
            print("Client Terminating.")
            break
        else:
            print(f"Message received from Queue - {msg}")


if __name__ == "__main__":

    queue = Queue()
    sender_process = Process(target = sender, args=(queue,))
    reader_process = Process(target = reader, args = (queue,))

    sender_process.start()
    reader_process.start()

    sender_process.join()
    reader_process.join()