import socket

MAXBYTES = 65535


def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    while True:
        text = input('Número: ')
        sock.sendto(text.encode(), ('127.0.0.1', 50000))
        print('Meu endereço é: ', sock.getsockname())
        data, address = sock.recvfrom(65535)
        print('Servidor responde: {}'.format(data.decode()))
    sock.close()
    return 0

if __name__ == '__main__':
    main()
