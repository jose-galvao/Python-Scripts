import socket

def recvall(sock, unid_milhar):
    data = b""
    while len(data) < unid_milhar:
        more = sock.recv(unid_milhar - len(data))
        if not more:
            EOFError("Cliente não digitou as unidades suficientes")

        data += more

    return data

def valores(num1,num2):

    return int(num1)+int(num2)


def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(('127.0.0.1', 50000))
    sock.listen(1)

    print("Ouvindo em", sock.getsockname())

    sc, sockname = sock.accept()
    dados=[]
    comprimento=0
    countdados=0
    compricliente=0
    while True:
        if(comprimento==0):
            comprimento += int(sc.recv(5).decode())
        elif(countdados < 2):
            dados.append(recvall(sc, comprimento))
            countdados+=1
        elif(compricliente == 0):
            compricliente=str(valores(dados[0], dados[1]))
            compritotal=str(len(compricliente))
            sc.sendall(compritotal.encode())
        else:
            soma=str(valores(dados[0], dados[1]))
            sc.sendall(soma.encode())

    sc.close()
    return 0

if __name__ == '__main__':
	main()