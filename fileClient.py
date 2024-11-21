import socket

def Client(filename):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    client.connect(("localhost",5000))

    # with open(filename,"r") as f:
    #     data = f.read(1024)
    #     client.sendall(data.encode('utf-8'))

    with open(filename, "rb") as f:
        client.sendfile(f)
    
    client.shutdown(socket.SHUT_WR)

    msg = client.recv(1024).decode('utf-8')
    print("Message from Server: ",msg)

if __name__ == "__main__":
    with open("Send.txt","w") as f:
        f.write("Message from Client - file to be saved locallyyyy - he he he")

    Client("Send.txt")
