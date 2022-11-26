import socket

MAXBYTES = 65535


def recvall(sock, length):
    data = b""
    while len(data) < length:
        more = sock.recv(length - len(data))

        if not more:
            raise EOFError("Cliente não enviou todos os dados esperados")
        data += more
    return data


def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(('0.0.0.0', 50000))
    data, address = sock.recvfrom(MAXBYTES)
    sock.sendto(b'', address)

    sock_comunicaco = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock_comunicaco.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock_comunicaco.bind(('127.0.0.1', 50001))
    sock_comunicaco.listen(1)
    while True:
        sc, sockname = sock_comunicaco.accept()
        msg = recvall(sc, 13)
        print("Mensagem recebida: ", msg.decode())
        sc.sendall("Oi, Cliente".encode())
        break
    return 0


if __name__ == '__main__':
    main()