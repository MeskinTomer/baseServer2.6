
import socket
MAX_PACKET = 1024
COMMANDS = ['TIME', 'NAME', 'RAND', 'EXIT']

def command():
    com = input("Enter the desired command")
    if (com in COMMANDS):
        return com
    else:
        return None


def main():
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        my_socket.connect(('127.0.0.1', 1729))
        my_socket.send(command().encode())
        response = my_socket.recv(MAX_PACKET).decode()
        print(response)
    except socket.error as err:
        print("recevied socket error " + str(err))
    finally:
        my_socket.close



if __name__ == '__main__':
    main()