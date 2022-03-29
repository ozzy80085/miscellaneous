import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(("www.google.com", 80))

request = f"GET / HTTP/1.1\r\nHost:www.google.com\r\n\r\n"

s.send(request.encode())

response = s.recv(4096)
response = response.decode(encoding="utf-8")

print(response)
