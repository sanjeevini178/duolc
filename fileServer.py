import socket

def Server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("localhost", 5000))

    server_socket.listen(1)

    print("Server connected at 5000")

    conn, addr = server_socket.accept()
    print(f"Connection established at {addr}")

    msg = conn.recv(1024).decode("utf-8")
    with open("Received.txt", "w") as f:
        f.write(msg)

    print(msg)
    conn.send("File Data written successfully!".encode("utf-8"))

Server()