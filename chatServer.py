import threading, socket

clients = []

def handle_client(conn, addr):
    print(f"Connection established with at {addr}")

    while True:
        try:
            msg = conn.recv(1024).decode("utf-8")
            print(f"Message received from {addr}: {msg}")
            Broadcast(conn, msg)
        except:
            break

    clients.remove(conn)

def Broadcast(conn, msg):
    for client in clients:
        if client != conn:
            client.send(msg.encode("utf-8"))

if __name__ == "__main__":

    server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_sock.bind(("localhost", 5000))
    server_sock.listen()

    while True:
        conn, addr = server_sock.accept()
        clients.append(conn)

        threading.Thread(target = handle_client, args = (conn, addr)).start()


