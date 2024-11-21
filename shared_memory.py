import time
from multiprocessing import Process, shared_memory

shm_name = "SharedMemory"

def writer():

    try:

        shm = shared_memory.SharedMemory(name = shm_name, create = True, size=1024)

        message = b"Hello from Writer!"

        shm.buf[:len(message)] = message

        print("Message from Writer written in Shared Memory")

        time.sleep(5)

    finally:

        shm.close()
        shm.unlink()

def reader():

    time.sleep(1)
    shm = shared_memory.SharedMemory(name = shm_name)

    try:
        message = bytes(shm.buf[:]).rstrip(b"\x00").decode("utf-8")
        print(f"Message read by reader - {message}")

    finally:
        shm.close()

if __name__ == "__main__":
    writer_process = Process(target=writer)
    reader_process = Process(target=reader)

    writer_process.start()
    reader_process.start()

    writer_process.join()
    reader_process.join()
