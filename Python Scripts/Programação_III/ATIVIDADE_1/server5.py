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
        if resultado >= 70:
            new_data = ('{} foi aprovado(a), a média foi {}'.format(nome, resultado))
        else:
            new_data = 'Você está em recuperação.'
            sock.sendto(new_data.encode(), address)
            data, address = sock.recvfrom(MAXBYTES)
            nrec = data.decode()
            nrec = int(nrec)
            notafinal = (nrec + resultado) / 2
            if notafinal >= 70:
                new_data = ('{} foi aprovado(a), a média foi {}'.format(nome, notafinal))
            else:
                new_data = ('{} foi reprovado(a), a média foi {}'.format(nome, notafinal))
        sock.sendto(new_data.encode(), address)
    socket.close()
    return 0
if __name__ == '__main__':
    main()