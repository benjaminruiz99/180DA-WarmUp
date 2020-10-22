# Reminder: This is a comment. The first line imports a default library "socket" into Python
# You don't install this. The second line is initialization to add TCP/IP protocol to the endpoint
import socket
serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Assigns a port for the server that listens to clients connecting to this port.
host = '192.168.1.23'
serv.bind((host,  4056))
serv.listen(5)
while True:
    conn, addr = serv.accept()
    from_client = ''
    while True:
        data = conn.recv(4096)
        if not data:
            break
        from_client += data.decode()
        print(from_client)
        server_message = 'I am SERVER\n'
        conn.send(server_message.encode())
    conn.close()
    print('client disconnected')
