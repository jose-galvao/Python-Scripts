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

    numero = 0
    count = 0
    mensagem = 0
    while True:
        if (numero == 0):
            numero = 1
            print("Digite o mensagem da mensagem")
            mensagem = str(input(''))
            sock.sendall(mensagem.encode())
        elif (count < 2):
            count += 1
            print("Digite um numero ")
            numero = str(input(''))

            sock.sendall(numero.encode())
        elif(mensagem == 0):
            mensagem=sock.recv(5)
            mensagem=int(str(mensagem.decode()))

        else:
            print("Soma do numero é: ", recvall(sock, mensagem).decode())
            break

    sock.close()
    return 0

if __name__ == '__main__':
	main()