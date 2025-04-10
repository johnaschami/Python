# USING PYTHON TO ACCESS WEB DATA

# Sockets in Python (Python has a built in support for TCP Scokets)

import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect( ("data.pr4e.org", 80))


