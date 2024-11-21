import socket

def client():

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    port = 8000
    client.connect(("localhost", port))

    print(f"Client connection on {port}")

    while True:
        
        message = input("Enter Message for server: ")

        client.send(message.encode())
        print(f"Message sent to server - {message}")

        if message.lower() == "quit":
            client.close()
            print("Connection closed.")
            break

        server_msg = client.recv(1024).decode()
        print(f"Server message: {server_msg}")


client()