""" Exercise1:   Inter-Process Communication in Distributed Computing
Objective:
To understand and implement inter-process communication using Java sockets.
To explore and implement Remote Method Invocation (RMI) for distributed computing.
Task 1: Build a Simple Client-Server Application
Description: Create a simple client-server application where the server provides a service and the client communicates with it.
Task 2: Enhanced Communication with Data Transfer
Description: Modify the client-server application to send and receive user-defined objects using ObjectInputStream and ObjectOutputStream.
Part 2: Remote Method Invocation (RMI)
Task 1: Create an RMI Service
Description: Develop an RMI-based distributed application where the server provides a remote service, and the client invokes this service.

Solution:
Part 1: Inter-Process Communication using Python Sockets
Task 1: Simple Client-Server Application
Server Code (Python): """
import socket


def simple_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 5000))
    server_socket.listen(1)
    
    print("Server is listening on port 5000...")
    
    connection, address = server_socket.accept()
    print(f"Connection from {address} has been established.")


    client_message = connection.recv(1024).decode('utf-8')
    print(f"Client says: {client_message}")
    
    server_message = "Hello from the server!"
    connection.sendall(server_message.encode('utf-8'))
    
    connection.close()
    server_socket.close()


if __name__ == "__main__":
    simple_server()
