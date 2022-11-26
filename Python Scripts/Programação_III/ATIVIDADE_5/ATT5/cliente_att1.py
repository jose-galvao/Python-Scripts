import socket
import zlib
import json
import struct


def recvall(sock, length):
    data = b""
    while len(data) < length:
        more = sock.recv(length - len(data))
        if not more:
            raise EOFError("Falha ao receber os dados esperados.")
        data += more
    return data

def recvmsg(sock):
    tam = struct.unpack("!i", recvall(sock, 4))[0]
    return recvall(sock, tam)

def sendmsg(sock, msg):
    sock.sendall(struct.pack("!i", len(msg)))
    sock.sendall(msg)

def compress(msg):
    return zlib.compress(msg)

def descompress(msg):
    return zlib.descompress(msg)

def toJSON(msg):
    return json.dumps(msg)

def fromJSON(msg):
    return json.loads(msg)

def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('127.0.0.1', 50000))


    dadosAlunos = []
    while True:

        nome = input("Nome do aluno: ")
        if not nome:
            break
        n1 = input("Nota 1: ")
        n2 = input("Nota 2: ")
        n3 = input("Nota 3: ")
        dadosAlunos.append([nome,n1,n2,n3])

    sendmsg(sock, compress(str(dados_aluno).encode()))
    res = descompress(recvmsg(sock)).decode()
    dadosAlunos = eval(res)
    for aluno in dadosAlunoa:
        print("O aluno ",aluno[0]," obteve a média ",aluno[1])

    sock.close()

    return 0

if _name_ == '_main_':
    main()