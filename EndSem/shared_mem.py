import time
from multiprocessing import Process, shared_memory

shm_name = "SharedMemory"

def writer():

    try:
        shm = shared_memory.SharedMemory(name=shm_name, create=True, size = 1024)

        msg = b"Hello from Writer Process!"
        shm.buf[:len(msg)] = msg

        print("Message written to memory!")

        time.sleep(5)

    finally:

        shm.close()
        shm.unlink()

def reader():

    time.sleep(1)
    shm = shared_memory.SharedMemory(name = shm_name)

    try:
        msg = bytes(shm.buf[:]).rstrip(b"x\00").decode("utf-8")

        print(f"Message Read -- {msg}")

    finally:
        shm.close()

if __name__ == "__main__":

    p1 = Process(target = writer)
    p2 = Process(target = reader)

    p1.start()
    p2.start()

    p1.join()
    p2.join()
