import socket

def client():
    
    client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_sock.connect(("localhost", 8000))

    print("Connection established!")

    while True:

        msg = input("Enter message: ")
        client_sock.send(msg.encode("utf-8"))

        if msg.lower() == "quit":
            break

        server_msg = client_sock.recv(1024).decode()
        print(f"Server Message -- {server_msg}")

    client_sock.close()

client()