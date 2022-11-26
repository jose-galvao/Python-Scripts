import socket

def conv(data):
    return data.decode()
def string(data):
    return len(data)

def recvall(sock, caractere):
    length=30
    data = b""
    while len(data) < length:
        more = sock.recv(length - len(data))
        if not more:
            EOFError("Cliente não enviou todos os dados esperados")

        data += more
    data +=caractere.encode()
    return data

def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(('127.0.0.1', 50000))
    sock.listen(1)

    print("Ouvindo em", sock.getsockname())

    while True:
        sc, sockname = sock.accept()
        print("Aceitando conexão de ", sockname)
        print("  Nome do Socket: ", sc.getsockname())
        print("  Host Remoto: ", sc.getpeername())
        msg = recvall(sc, ".")
        print("Mensagem recebida: ", msg)
        sc.sendall(msg)
        sc.close()

    return 0



if __name__ == '__main__':
    main()