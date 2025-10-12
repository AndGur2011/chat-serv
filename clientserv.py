import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost", 4444))
client_name = input("Як тебе звуть")
client.send(client_name.encode())
 
while True:
    try:
        answer_from_servak = client.recv(1024).decode()
        print(answer_from_servak)
    except:
        pass
