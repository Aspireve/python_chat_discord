import socket
import threading
def write():
    while True:
        message = '{}: {}'.format(user_name, input(''))
        client.send(message.encode('ascii'))

def receive():
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            if message == 'server_gen_nick':
                client.send(user_name.encode('ascii'))     # to send user_name back
            else:
                print(message)
        except:
            print("An error occured!")
            client.close()
            break


user_name = input("Choose your user name: ")
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 55555))

# GOTO learn these
receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()




