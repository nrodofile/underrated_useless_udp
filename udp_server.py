__author__ = 'Nicholas Rodofile'
import subprocess
import threading, time

def play(file):
    return subprocess.call(["afplay", file])


def alien():
    audio_file = "Get Away From Her You Bitch.mp3"
    return play(audio_file)

def intrud():
    audio_file = "intruder_alert_.mp3"
    return play(audio_file)


def lucky():
    audio_file = "Do You Feel Lucky, Punk-.mp3"
    return play(audio_file)


def money():
    audio_file = "Show Me The money.mp3"
    return play(audio_file)


def hello():
    audio_file = "Scarface - Say Hello To My Little Friend.mp3"
    return_code = subprocess.call(["afplay", audio_file])
    return return_code


def back():
    audio_file = "I_ll be Back.mp3"
    return play(audio_file)


def bye():
    audio_file = "Hasta La Vista Baby.mp3"
    return play(audio_file)

import SocketServer

class MyUDPHandler(SocketServer.BaseRequestHandler):
    """
    This class works similar to the TCP handler class, except that
    self.request consists of a pair of data and client socket, and since
    there is no connection the client address must be given explicitly
    when sending data back via sendto().
    """

    def handle(self):
        data = self.request[0].strip()
        socket = self.request[1]
        print "{} wrote:".format(self.client_address[0])
        print data
        if "alien" in data:
            threading.Thread(target=alien).start()
        if "lucky" in data:
            threading.Thread(target=lucky).start()
        if "hello" in data:
            threading.Thread(target=hello).start()
        if "money" in data:
            threading.Thread(target=money).start()
        if "bye" in data:
            threading.Thread(target=bye).start()
        if "back" in data:
            threading.Thread(target=back).start()
        if "intrud" in data:
            threading.Thread(target=intrud).start()
        socket.sendto(data.upper(), self.client_address)

if __name__ == "__main__":
    HOST, PORT = "localhost", 9999
    server = SocketServer.UDPServer((HOST, PORT), MyUDPHandler)
    server.serve_forever()