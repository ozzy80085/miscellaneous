import socket

host = "0.0.0.0"
port = 8080

file = open("index.html", "r")
html = file.read()
file.close()

html = bytes(html, "utf-8")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
print(f"Listening for incoming connections on {host}:{port}")

while True:
	s.listen()
	conn, addr = s.accept()

	with conn:
		print(f"Connected by {addr}")
		conn.sendall(str.encode("HTTP/1.0 200 OK\n",'utf-8'))
		conn.sendall(str.encode('Content-Type: text/html\n', 'utf-8'))
		conn.send(str.encode('\r\n'))
		conn.sendall(html)
		#conn.close()
