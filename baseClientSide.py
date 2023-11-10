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


def command(com):
    """
    validates the command from the user
    :param com: The command entered by the user
    :type: string
    :return: either the validated command or either "Invalid" for invalid commands
    """
    if com not in COMMANDS:
        com = 'Invalid'
    return com


def protocol_send(message):
    message_len = len(message)
    final_message = str(message_len) + '!' + message
    return final_message


def protocol_receive(my_socket):
    cur_char = ''
    message_len = ''
    while cur_char != '!':
        cur_char = my_socket.recv(1).decode()
        message_len += cur_char
    message_len = message_len[:-1]
    return my_socket.recv(int(message_len)).decode()


def main():
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        my_socket.connect(('127.0.0.1', 1729))
        while True:
            com = input("Enter the desired command")
            com = command(com)
            if com != 'Invalid':
                my_socket.send(protocol_send(com).encode())
                logging.debug('The command ' + com + ' has been sent to the server')
                response = protocol_receive(my_socket)
                logging.debug('The response ' + response + ' has been received')
                print(response)
                if response == 'You were disconnected':
                    logging.debug('The server has disconnected the client')
                    break
            else:
                logging.debug('Invalid command has attempted to be sent')
                print('Invalid command')
    except socket.error as err:
        logging.error('Received socket error ' + str(err))
        print("Received socket error " + str(err))
    finally:
        my_socket.close()
        logging.debug('The client socket has been closed')


if __name__ == '__main__':
    assert command('TIME') == 'TIME'
    assert command('NAME') == 'NAME'
    assert command('RAND') == 'RAND'
    assert command('EXIT') == 'EXIT'
    assert command('BAND') == 'Invalid'
    assert protocol_send('hello') == '5!hello'
    main()
