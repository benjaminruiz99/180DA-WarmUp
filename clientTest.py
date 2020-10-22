import socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '192.168.1.23'
client.connect((host, 4056))
client_message = 'I am CLIENT\n'
client.send(client_message.encode())
from_server = client.recv(4096)
client.close()
print(from_server.decode())
