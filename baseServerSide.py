

import logging
import socket
import random
from datetime import datetime


MAX_PACKET = 4
QUEUE_LEN = 1
NAME = "my name is jef"


def time():
    """
    Returns the current time
    :param time_and_date: gets the current time and date
    :type param time_and_date: string
    :param current_time: the current time seperated from the date
    :type paran current_time: string
    :return: current_time - the time seperated into hours, minutes and seconds
    """
    time_and_date = datetime.now()
    current_time = time_and_date.strftime('%H:%M:%S')
    return current_time


def rand():
    """
    Generates a random number between 1 and 10
    :param random_num: the generated random number
    :type param random_num: int
    :return: random_num - the random num
    """
    random_num = random.randint(1, 11)
    return str(random_num)


def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        server_socket.bind(('0.0.0.0', 1729))
        server_socket.listen(QUEUE_LEN)
        while True:
            client_socket, client_address = server_socket.accept()
            try:
                request = client_socket.recv(MAX_PACKET).decode()
                print('Received the command: ' + request)
                if(request == 'TIME'):
                    client_socket.send(time().encode())
                elif(request == 'NAME'):
                    client_socket.send(NAME.encode())
                elif(request == 'RAND'):
                    client_socket.send(rand().encode())
                elif(request == 'EXIT'):
                    return
                else:
                    client_socket.send('Invalid command'.encode())
            except socket.error as err:
                print('received socket error on client socket' + str(err))
            finally:
                client_socket.close()
    except socket.error as err:
        print('received socket error on server socket' + str(err))
    finally:
        server_socket.close

if __name__ == '__main__':
    main()

