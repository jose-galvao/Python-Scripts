import socket

MAXBYTES = 65535
def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(('127.0.0.1', 50001))

    while True:
        data, address = sock.recvfrom(MAXBYTES)
        new_data = data.decode().split(' ')
        nome = new_data[0]
        nota1 = int(new_data[1])
        nota2 = int(new_data[2])
        resultado = (nota1 + nota2) / 2
        new_data = ('A média do aluno {}, é {}'.format(nome, resultado))
        sock.sendto(new_data.encode(), address)
    socket.close()
    return 0
if __name__ == '__main__':
    main()