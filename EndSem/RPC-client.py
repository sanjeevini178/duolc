import socket, pickle

fun = input("Enter add or sub: ")
a = int(input("Enter Param 1: "))
b = int(input("Enter Param 2: "))

dic = {"Function":fun, "args":[a, b]}

dic = pickle.dumps(dic)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost", 6000))

client.send(dic)

msg = client.recv(1024).decode("utf-8")
print(f"Server message -- {msg}")

client.close()