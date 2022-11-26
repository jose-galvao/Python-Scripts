import socket
def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(('127.0.0.1', 50000))
    sock.listen(1)

    print("Ouvindo em", sock.getsockname())
    return 0
def converterByteToString(data):
    return data.decode()
def tamanhoString(data):
    return len(data)
def buscarMaior(numero_um,numero_dois):
    n1=int(converterByteToString(numero_um))
    n2=int(converterByteToString(numero_dois))

    if(n1<n2):
        return str(n1)
    else:
        return str(n2)

def recvall(sock, unid_milhar):
    data = b""
    while len(data) < unid_milhar:
        more = sock.recv(unid_milhar - len(data))
        if not more:
            EOFError("Cliente não digitou as unidades suficientes")

        data += more

    return data

if __name__ == '__main__':
    main()