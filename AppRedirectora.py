#!/usr/bin/python

"""
Nerea Del Olmo Sanz - GITT
Ejercicio 14.4

Servidor de aplicaciones con redireccionamiento.

Este ejercicio hace que el servidor entre en un bucle
infinito de redireccionamiento. Los navegadores son capaces
de detectarlo, por lo que tras X intentos, rechazan la
conexión.
1 petición del recurso / + 20 redirecciones
"""

import socket
import random

# Create a TCP objet socket and bind it to a port
# Port should be 80, but since it needs root privileges,
# let's use one above 1024

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Let the port be reused if no process is actually using it
mySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# Bind to the address corresponding to the main name of the host
hostname = socket.gethostname() #"localhost"
port = 1235
mySocket.bind((hostname, port))

# Queue a maximum of 5 TCP connection requests

mySocket.listen(5)

# Accept connections, read incoming data, and answer back an HTML page
#  (in an almost-infinite loop; the loop can be stopped with Ctrl+C)

try:
    while True:
        print 'Waiting for connections'
        (recvSocket, address) = mySocket.accept()
        print 'Request received:'
        print recvSocket.recv(2048)
        print 'Answering back...'
        RandomNumber = 100000000 * random.random()
        URL = "http://" + str(hostname) + ":" + str(port)
        RandomURL =  URL +"/" + str(RandomNumber)
        recvSocket.send("HTTP/1.1 302 FOUND \r\n" +
                        "Location: " + RandomURL + "\r\n" +
                        "<html><TITLE>Nerea's first server</TITLE>" +
                        "<body><h1>Redireccionamiento</A></h1></p>"
                        "<p><I>Nerea Del Olmo Sanz</I></p></body></html>\r\n")
        recvSocket.close()
except KeyboardInterrupt:
    print "Closing binded socket"
    mySocket.close()
