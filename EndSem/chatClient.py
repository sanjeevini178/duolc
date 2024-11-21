import threading, socket

def Receive(client_sock):

    msg = client_sock.recv(1024).decode("utf-8")
    print(f"Message from Server -- {msg}")
    print("\n")
    Send(client_sock)

def Send(client_sock):

    msg = input("Enter message: ")
    client_sock.send(msg.encode("utf-8"))

if __name__ == "__main__":

    client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_sock.connect(("localhost", 5000))

    while True:
        t1 = threading.Thread(target = Receive, args = (client_sock, )).start()
        Send(client_sock)