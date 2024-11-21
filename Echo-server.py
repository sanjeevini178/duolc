import socket

def server():

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server.bind(("localhost", 8000))
    server.listen(1)

    print("Server listening on port 8000")

    conn, address = server.accept()

    print(f"Client connected on {address}")

    while True:
        client_msg = conn.recv(1024).decode()

        print(f"Message from client - {client_msg}")

        if client_msg.lower() == "quit":
            conn.close()
            server.close()
            print("Server closed.")
            break
        
        else:
            conn.send(client_msg.encode())
            print(f"Message echoed to Client - {client_msg}")


server()