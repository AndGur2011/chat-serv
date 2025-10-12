import socket
import threading

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 1028))
server.setblocking(False)
server.listen(5)
print("Работа")
clients = []

def accept_messages():
    while True:
        try:
            for client in clients:
                sended_message = client.recv(1024).decode()
                print(sended_message)
                if sended_message == "привіт":
                    client.send("вітаю".encode())
                elif sended_message == "як справи?":
                    client.send("усе добре, дякую!".encode())
                elif sended_message == "да?":
                    client.send("да и ., нет ДА и !!!".encode())
                else:
                    client.send("я не розумію цю команду".encode())
        except:
            pass
threading.Thread(target = accept_messages).start()
while True:
    try:
        information, ip_conect = server.accept()
        print("До мене підключився кліент:", ip_conect)
        information.setblocking(False)
        clients.append(information)
    except:
        pass
