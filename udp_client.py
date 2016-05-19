import socket

HOST, PORT = "localhost", 9999
while True:
    data = str(raw_input(">"))
    # SOCK_DGRAM is the socket type to use for UDP sockets
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # As you can see, there is no connect() call; UDP has no connections.
    # Instead, data is directly sent to the recipient via sendto().
    sock.sendto(data + "\n", (HOST, PORT))
    received = sock.recv(1024)

    print "Received: {}".format(received)