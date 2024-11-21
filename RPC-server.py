import socket, pickle

def add(a,b):
    c = a + b
    return c

def sub(a,b):
    c = a - b
    return c

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(("localhost", 5000))
server.listen(1)

conn, addr = server.accept()
print(f"Connection established at {addr}")

rec_dic = conn.recv(1024)

rec_dic = pickle.loads(rec_dic)

fun = rec_dic["Function"]
a = rec_dic["args"][0]
b = rec_dic["args"][1]

if fun == "add":
    result = add(a,b)
    print(result)

elif fun == "sub":
    result = sub(a,b)

conn.send(str(result).encode("utf-8"))

conn.close()
server.close()

