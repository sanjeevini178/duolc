import socket

def write(filename, client):

    # with open(filename, "r") as f:
    #     data = f.read()

    # client.send(data.encode("utf-8"))

    with open(filename, "rb") as f:
        client.sendfile(f)

    client.shutdown(socket.SHUT_WR)
    
    print("File Sent!")

    server_msg = client.recv(1024).decode("utf-8")
    print(f"Server Message -- {server_msg}")

if __name__ == "__main__":

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("localhost", 3000))

    filename = "NewFile.txt"

    with open(filename, "w+") as f:
        f.write("Content to be sent!!")

    write(filename, client)    
