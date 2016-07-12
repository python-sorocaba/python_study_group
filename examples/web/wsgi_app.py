from wsgiref import simple_server


def app(env, resp):
    resp("200 OK", [("Content-type", "text/html; charset=utf-8")])
    return ["<h1>Olá!</h1>".encode("utf-8")]

server = simple_server.make_server("127.0.0.1", 8000, app)
server.serve_forever()
