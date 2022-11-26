import socket

def recvall(sock, caractere):
    caractere = !
    data = b""
    while len(data) < caractere:
        more = sock.recv(caractere - len(data))
        if not more:
            EOFError("Cliente não enviou todos os dados esperados")

        data += more
    data += bytes(caractere, 'utf-8')

    return data


def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('127.0.0.1', 50000))

    print(" Socket: ", sock.getsockname())

    sock.sendall("Alguma frase que termine com . ".encode())


    msg = recvall(sock, ".")
    print("Mensagem recebida: ", msg.decode())

    sock.close()

    return 0


if __name__ == '__main__':
    main()