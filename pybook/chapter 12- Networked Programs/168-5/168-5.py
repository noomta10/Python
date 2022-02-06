import socket

url = input("Enter URL: ")
url_divided = url.split("/")
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect((url_divided[2], 80))
cmd = 'GET {} HTTP/1.0\r\n\r\n'.format(url).encode()
mysock.send(cmd)
url_text = ""

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    data = data.decode()
    url_text += data

new_line_index = url_text.find("\r\n\r\n")
data_beginning_index = new_line_index + 4
print(url_text[data_beginning_index:])

mysock.close()