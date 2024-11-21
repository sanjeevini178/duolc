import socket

def server():

    server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_sock.bind(("localhost", 8000))
    server_sock.listen(1)

    conn, addr = server_sock.accept()
    print(f"COnnection established at {addr}")

    while True:
        msg = conn.recv(1024).decode()
        if msg.lower() == "quit":
            print("Termination Signal Received.")
            break

        print(f"Message from client -- {msg}")
        server_msg = "Message Received."
        conn.send(server_msg.encode("utf-8"))
        
    conn.close()
    server_sock.close()

server()


                  
