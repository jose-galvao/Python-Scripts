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


def find_server(sock):
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    delay = 0.1

    while True:
        sock.sendto(b"DISCOVERY", ('127.255.255.255', 50000))
        sock.settimeout(delay)

        try:
            data, address = sock.recvfrom(MAXBYTES)
        except socket.timeout:
            delay *= 2
            print("Servidor não encontrado!")
        else:
            print("Servidor encontrado em {}".format(address))
            break
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 0)
    sock.settimeout(None)

    return address


def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    address = find_server(sock)
    sock.connect(address)

    sock_comunicao = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock_comunicao.connect(('127.0.0.1', 50001))

    while True:
        sock_comunicao.sendall("Oi, Servidor!".encode())
        mgs_servidor=   recvall(sock_comunicao, 11)
        print("Mensagem:",mgs_servidor.decode())
        break
    sock.close()
    return 0


if __name__ == '__main__':
    main()