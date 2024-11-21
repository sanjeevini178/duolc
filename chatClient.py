import threading, socket

def Receive(client_sock):

    msg = client_sock.recv(1024).decode("utf-8")
    print(f"Message Received from Server - {msg}")
    print("\n")
    Send(client_sock)

def Send(client_sock):
    msg = input("Enter your text: ")
    client_sock.send(msg.encode("utf-8"))

if __name__ == "__main__":

    client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    client_sock.connect(("localhost", 5000))
    print("Client connection at port 5000.")

    while True:
        threading.Thread(target=Receive, args = (client_sock, )).start()
        Send(client_sock)