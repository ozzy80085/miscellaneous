import socket

#the following sends the specified message then close the connection but continue to listen for incomming connections
#i cant think of a reason when this would be useful but you never know


HOST = "127.0.0.1"  
PORT = 23

msg = b"""

Hello World!

"""

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))

while True:
    s.listen()
    conn, addr = s.accept()
    
    with conn:
        print(f"Connected by {addr}")
        conn.sendall(msg)
        conn.close()
