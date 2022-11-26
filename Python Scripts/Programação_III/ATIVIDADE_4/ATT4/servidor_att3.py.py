import socket
import pickle



def verificarDelimitador(dados, delimitador):
    data_dados=dados

    if(data_dados.count(delimitador)>=1):
        return True
    return False


def recvall(sock, delim):
    data = b""
    while True:
        more = sock.recv(1)
        data += more

        if(verificarDelimitador(data.decode('ISO-8859-1'), delim.decode())):
            break

    return data.decode().replace("<FIM>","")



def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(('127.0.0.1', 50000))
    sock.listen(1)

    print("Ouvindo em", sock.getsockname())

    while True:
        sc, sockname = sock.accept()

        print(recvall(sc, b"<FIM>"))

        sc.sendall("É sim!<FIM>".encode())

        print(recvall(sc, b"<FIM>"))
        sc.sendall("É sim!<FIM>".encode())

        print(recvall(sc, b"<FIM>"))
        sc.sendall("É sim!<FIM>".encode())

        sc.close()

    return 0
if __name__ == '__main__':
    print("Servidor ligado")
    main()