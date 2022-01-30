import socket

url = input("Enter URL: ")
url_divided = url.split("/")
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect((url_divided[2], 80))
cmd = 'GET {} HTTP/1.0\r\n\r\n'.format(url).encode()
mysock.send(cmd)
character_count = 0

while True:
    data = mysock.recv(500)
    character_count += len(data)
    if character_count <= 3000:
        print(data.decode(), end='')
    if len(data) < 1:
        break
print("\nTotal number of characters: {}".format(character_count))

mysock.close()
