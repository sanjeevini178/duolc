import socket, pickle

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost", 5000))

fun = input("Enter Function name: ")
par1 = int(input("Enter Param 1: "))
par2 = int(input("Enter Param 2: "))

dic = {"Function" : fun, "args" : [par1, par2]}
dic = pickle.dumps(dic)

client.send(dic)

result = client.recv(1024).decode("utf-8")
print(result)

client.close()
