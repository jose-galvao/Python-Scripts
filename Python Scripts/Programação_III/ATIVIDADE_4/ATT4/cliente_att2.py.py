import socket
import struct


def recvall(sock, length):
    data = b""
    while len(data) < length:
        more = sock.recv(length - len(data))

        if not more:
            raise EOFError("Falha ao receber os dados esperados.")
        data += more
    return data


def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('127.0.0.1', 50000))

    print(" Socket: ", sock.getsockname())

    msg = struct.pack("!iis", 600, 300,'-'.encode())
    print("Enviando dois Operandos e um operador.")
    sock.sendall(msg)

    res = recvall(sock,4)
    print("Resultado da operacao : ", struct.unpack("!i", res)[0])

    sock.close()

    return 0

if __name__ == '__main__':
    print("Cliente ligado")
    main()