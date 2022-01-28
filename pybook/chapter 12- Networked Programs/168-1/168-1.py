import socket

url = input("Enter URL: ")
url_divided = url.split("/")
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect((url_divided[2], 80))
cmd = 'GET {} HTTP/1.0\r\n\r\n'.format(url).encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(),end='')

mysock.close()