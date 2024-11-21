import socket

def read(conn):

    data = conn.recv(1024).decode("utf-8")

    with open("CreatedFile.txt", "w+") as f:
        f.write(data)

    msg = f"Data Received -- {data}"
    print(msg)

    conn.send(msg.encode("utf-8"))

if __name__ == "__main__":

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server.bind(("localhost", 3000))
    server.listen()

    conn, addr = server.accept()

    read(conn)