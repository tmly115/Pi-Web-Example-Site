from server import Server
from server.html_template import HTML_Template

HOST = "127.0.0.1"
PORT = 80

server = Server(HOST, PORT)

index = HTML_Template("templates/index.html")
contact_me = HTML_Template("templates/contact_me.html")

server.add_page("/", index.generate_html())
server.add_page("/contact_me", contact_me.generate_html())

server.start_server()
server.stop_server()

