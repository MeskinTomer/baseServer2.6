"""
Author: Tomer Meskin
Date: 03/11/2023
Description: The program acts as the client side of a base server that accepts 4 commands:
TIME: sends the current time
RAND: generates a random number between 1 - 10
NAME: sends the name of the server
EXIT: disconnects the client from the server
The client is able to send multiple commands until the command 'EXIT', while the server is able to connect
to one client after another.
"""

import socket
import logging

logging.basicConfig(filename='baseClient_log.log', level=logging.DEBUG)

MAX_PACKET = 1024
COMMANDS = ['TIME', 'NAME', 'RAND', 'EXIT']


def command():
    """
    validates the command from the user
    :return: either the validated command or either "Invalid" for invalid commands
    """
    com = input("Enter the desired command")
    if com in COMMANDS:
        return com
    else:
        return 'Invalid'


def main():
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        my_socket.connect(('127.0.0.1', 1729))
        while True:
            com = command()
            if com != 'Invalid':
                my_socket.send(com.encode())
                logging.debug('The command ' + com + ' has been sent to the server')
                response = my_socket.recv(MAX_PACKET).decode()
                logging.debug('The response ' + response + ' has been received')
                print(response)
                if response == 'You were disconnected':
                    logging.debug('The server has disconnected the client')
                    break
            else:
                print('Invalid command')
    except socket.error as err:
        logging.error('Received socket error ' + str(err))
        print("Received socket error " + str(err))
    finally:
        my_socket.close()
        logging.debug('The client socket has been closed')


if __name__ == '__main__':
    main()
