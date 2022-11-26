import socket


def recvall(sock, length):
    data = b""
    while len(data) < length:
        more = sock.recv(length - len(data))

        if not more:
            raise EOFError("Cliente não enviou todos os dados esperados")
        data += more
    return data


def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('127.0.0.1', 50000))

    print(" Socket: ", sock.getsockname())
    mensagem=0
    caracter=0
    while True:
        if(caracter==0):
            sock.sendall("!".encode())
            caracter=1
        elif(mensagem == 0):
            sock.sendall("Ola, pessoal!".encode())
            mensagem=1
        else:
            print(recvall(sock, 12).decode())
            break

    sock.close()

    return 0

if __name__ == '__main__':
	main()