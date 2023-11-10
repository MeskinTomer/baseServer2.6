"""
Author: Tomer Meskin
Date: 03/11/2023
Description: The program acts as the server side of a base server that accepts 4 commands:
TIME: sends the current time
RAND: generates a random number between 1 - 10
NAME: sends the name of the server
EXIT: disconnects the client from the server
The client is able to send multiple commands until the command 'EXIT', while the server is able to connect
to one client after another.
"""

import socket
import logging
import random
from datetime import datetime

logging.basicConfig(filename='baseServer_log.log', level=logging.DEBUG)

MAX_PACKET = 4
QUEUE_LEN = 1
NAME = "my name is jef"


def time():
    """
    Returns the current time
    :return: current_time - the time separated into hours, minutes and seconds
    """
    time_and_date = datetime.now()
    current_time = time_and_date.strftime('%H:%M:%S')
    return current_time


def rand():
    """
    Generates a random number between 1 and 10
    :return: random_num - the random num
    """
    random_num = random.randint(1, 10)
    return str(random_num)


def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        server_socket.bind(('0.0.0.0', 1729))
        server_socket.listen(QUEUE_LEN)
        while True:
            client_socket, client_address = server_socket.accept()
            logging.debug('A client has connected to the server || address: ' + ''.join(map(str, client_address)))
            try:
                while True:
                    request = client_socket.recv(MAX_PACKET).decode()
                    logging.debug('The command ' + request + ' has been received')
                    print('Received the command: ' + request)
                    if request == 'TIME':
                        sent_message = time()
                    elif request == 'NAME':
                        sent_message = NAME
                    elif request == 'RAND':
                        sent_message = rand()
                    elif request == 'EXIT':
                        client_socket.send('You were disconnected'.encode())
                        break
                    else:
                        sent_message = 'Invalid command'
                    client_socket.send(sent_message.encode())
                    logging.debug('The message ' + sent_message + ' has been sent')
            except socket.error as err:
                print('received socket error on client socket' + str(err))
            finally:
                client_socket.close()
                logging.debug('The client has been disconnected')
    except socket.error as err:
        print('received socket error on server socket' + str(err))
    finally:
        server_socket.close()


if __name__ == '__main__':
    assert rand() in range(1, 11)
    assert NAME == 'my name is jef'
    main()
