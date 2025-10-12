import socket
servak= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servak.bind(("localhost", 4444))
servak.setblocking(False)

servak.listen(5)
print("Сервер очікує підключення")
clients = []

while True:
    
    try:
        info, ip_adress = servak.accept()
        print(f"До мене під'єднався кліент с ip{ip_adress}")
        info.setblocking(False)
        clients.append(info)
    except:
        pass
    
    for client in clients:
        try:
            client.send(f"Привіт {data} ви на сервері Тенни".encode())
        except:
            print("Від мене від'єдналася чукча")
            clients.remove(client)
rint("Ніхто не підключається")
data = info.recv(1024).decode()
print(data)

info.send(f"Привіт {data}".encode())

info.close()
servak.close()
