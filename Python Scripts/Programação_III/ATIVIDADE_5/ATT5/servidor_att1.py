import socket
import zlib
import json
import struct
import csv


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

def buscarDados():
    dados = []
    arquivos = open('notas.csv')

    linhas = csv.reader(arquivo)
    for linha in linhas:
        dados.append(linha)
    return dados

def addDados(dados):
    import csv
    file = open("notas.csv", "w")
    lista =  eval(dados)
    c = csv.writer(file)
    for i in lista:
        c.writerow(i)

def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(('127.0.0.1', 50000))
    sock.listen(1)

    print("Ouvindo em", sock.getsockname())

    while True:
        sc, sockname = sock.accept()
        addDados(decompress(recvmsg(sc)).decode())
        media = []
        for aluno in buscarDados():
            if(aluno!=[]):
                media.append([aluno[0],(float(aluno[1])+float(aluno[2])+float(aluno[3]))/3])
        print(media)
        sendmsg(sc, compress( str(media).encode()))

        sc.close()

    return 0

if _name_ == '_main_':
    main()