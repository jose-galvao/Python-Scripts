import socket

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
    sock.connect(('127.0.0.1', 50000))

    print(" Socket: ", sock.getsockname())

    sock.sendall("Python é bom demais.<FIM>".encode())
    print(recvall(sock, b"<FIM>"))

    sock.sendall("Sockets é bom demais.<FIM>".encode())
    print(recvall(sock, b"<FIM>"))

    sock.sendall("Framing é bom demais.<FIM>".encode())
    print(recvall(sock, b"<FIM>"))

    sock.close()

    return 0

if __name__ == '__main__':
    print("Servidor ligado")
    main()