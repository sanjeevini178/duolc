import socket, pickle

def add(a, b):
    sum = a + b
    return sum

def sub(a, b):
    diff = a - b
    return diff

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 6000))
server.listen()

conn, addr = server.accept()
print(f"Connection established at {addr}")

dic = conn.recv(1024)
dic = pickle.loads(dic)

fun = dic["Function"]
a = dic["args"][0]
b = dic["args"][1]

if fun == "add":
    data = add(a, b)
    print(f"Result -- {data}")
    conn.send(str(data).encode("utf-8"))
elif fun == "sub":
    data = sub(a, b)
    print(f"Result -- {data}")
    conn.send(data.encode("utf-8"))

conn.close()
server.close()


