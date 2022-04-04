import socket

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySocket.connect(('data.pr4e.org', 80))
command = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mySocket.send(command)

while True:
    webData = mySocket.recv(1024)
    if len(webData) < 1:
        break
    print(webData.decode())

mySocket.close()