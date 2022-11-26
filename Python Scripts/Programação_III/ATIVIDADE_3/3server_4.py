import socket


def recvall(sock, length):
    data = b""
    while len(data) < length:
        more = sock.recv(length - len(data))
        if not more:
            raise EOFError("Cliente não enviou todos os dados esperados")
        data += more



    return data


def recvall_(sock, length, carac):
    data = b""
    while len(data) < length:
        more = sock.recv(length - len(data))
        if not more:
            raise EOFError("Cliente não enviou todos os dados esperados")
        data += more
        mgs = data.decode()
        dado=""
        for i in mgs:
            if(i.__eq__(carac)):
                break
            dado+=i




    return dado

def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(('127.0.0.1', 50000))
    sock.listen(1)


    print("Ouvindo em", sock.getsockname())
    caracter= ''
    mensagem=''
    while True:
        sc, sockname = sock.accept()
        print("Aceitando conexão de ", sockname)
        print("  Nome do Socket: ", sc.getsockname())
        print("  Host Remoto: ", sc.getpeername())

        while True:
            if(caracter== ''):
                caracter=recvall(sc, 1).decode()
                print(caracter)

            elif(mensagem==""):
                mensagem = recvall_(sc, 13, caracter)

            else:
                mensagem=mensagem.upper()
                sc.sendall(mensagem.encode())
                break
        break

    return 0
if __name__ == '__main__':
	main()