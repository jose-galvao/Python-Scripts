import socket
def recvall(sock, length):

    data = b""
    while len(data) < length:
        more = sock.recv(length - len(data))
        if not more:
            EOFError("Cliente não enviou todos os dados esperados")

        data += more


    return data


def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('127.0.0.1', 50000))
    print(" Socket: ", sock.getsockname())

    qtd_digitados=0
    while True:
        if(qtd_digitados<2):
            print("Digite um numero")
            numero = str(input(''))
            sock.sendall(numero.encode())
            qtd_digitados+=1
        else:
            print("Numero maior é :",recvall(sock,4).decode())
            break


    sock.close()

    return 0


if __name__ == '__main__':
	main()