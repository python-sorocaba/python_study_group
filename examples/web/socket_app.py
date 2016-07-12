import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("127.0.0.1", 8000))
s.listen(1)
con, address = s.accept()

print(con, address)
data = con.recv(10000)

print(data.decode("utf-8"))
con.send("""HTTP/1.1 200 Ok
Content-Type: text/html; charset=utf-8

<h1>Olá!</h1>
""".encode("utf-8"))

con.close()
