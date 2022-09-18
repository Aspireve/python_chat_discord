from socket import socket
import threading
import socket

def handle(client):
    while True:
        try:
            message = client.recv(1024)
            for x in clients:
                if (x == client):
                    pass
                else:
                    x.send(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            for client in clients:
                client.send('{} left!'.format(nickname).encode('ascii'))
            nicknames.remove(nickname)
            break

def receive():
    while True:
        client, address = server.accept()
        print(client)
        print(f"Connected with {str(address)}")

        client.send('server_gen_nick'.encode('ascii'))
        nickname = client.recv(1024).decode('ascii')
        nicknames.append(nickname)
        clients.append(client)

        print("Nickname is {}".format(nickname))
        for x in clients:
            if(x!= client):
                x.send(f"\n\n{nickname} hopped onto this server!!\n\n".encode('ascii'))
            else:
                x.send(f"\n\n{nickname}, welcome to this server. Others have been informed about your presence!!\n\n".encode('ascii'))
        client.send('Connected to server!'.encode('ascii'))

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   #no idea what it does lol
server.bind(('127.0.0.1', 55555))
server.listen()                                              # makes the server listen to clients
clients = []          
nicknames = []
receive()






