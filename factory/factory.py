import time
import zmq
import os
import threading


def client_task():

    socket = zmq.Context().socket(zmq.REQ)
    socket.connect("ipc://soc.ipc")
    print("client started")
    for request in range(100):
        socket.send(b"Hello")

        #  Get the reply.
        message = socket.recv()
        print("Received reply %s [ %s ]" % (request, message))


def server_task():

    socket = zmq.Context().socket(zmq.REP)
    socket.bind("ipc://soc.ipc")
    print("server started")
    while True:
        #  Wait for next request from client
        message = socket.recv()
        print("Received request: %s" % message)

        #  Do some 'work'

        #  Send reply back to client
        socket.send(b"World")

def main():

    thread1 = threading.Thread(target=client_task)
    thread2 = threading.Thread(target=server_task)

    thread2.start()
    thread1.start()


if __name__ == "__main__":
    main()