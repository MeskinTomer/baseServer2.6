import sys
import logging
import socket
from datetime import datetime

MAX_PACKET = 4
QUEUE_LEN = 1


def main():
    server_socket = socket.socket(socket.AF_INET, socket.STREAM)
    try:
        server_socket.bind(('0.0.0.0', 1729))
        server_socket.listen(QUEUE_LEN)
        client_socket, client_address = server_socket.accept()
        try:
            request = client_socket.recv(MAX_PACKET).decode()
        except socket.error as err:
            print('received socket error on client socket' + str(err))
        finally:
            client_socket.close()
    except socket.error as err:
        print('recevied socket error on server socket' + str(err))
    finally:
        server_socket.close

if __name__ == '__main__':
    main()

