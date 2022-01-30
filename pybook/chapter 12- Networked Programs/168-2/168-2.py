import socket

url = input("Enter URL: ")
url_divided = url.split("/")
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
url_name = url_divided[2]
mysock.connect((url_name, 80))
cmd = 'GET {} HTTP/1.0\r\n\r\n'.format(url).encode()
mysock.send(cmd)
character_count = 0
printed = 0

while True:
    data = mysock.recv(1000)
    character_count += len(data)
    if printed < 3000:
        if character_count < 3000:
            print(data)
            printed += len(data)
        else:
            print(data[0:3000-printed])
            printed = 3000
    if len(data) < 1:
        break
print("\nTotal number of characters: {}".format(character_count))

mysock.close()
