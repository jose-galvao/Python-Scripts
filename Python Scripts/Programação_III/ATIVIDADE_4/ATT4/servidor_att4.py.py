# coding: utf-8

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

def recvmsg(sock):
    tam = struct.unpack("!i",recvall(sock,4))[0]
    return recvall(sock,tam)

def sendmsg(sock,msg):
    sock.sendall(struct.pack("!i",len(msg)))
    sock.sendall(msg)

def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(('127.0.0.1',50000))
    sock.listen(1)
    
    print("Ouvindo em", sock.getsockname())
    
    while True:
        sc, sockname = sock.accept()
         
        msg = recvmsg(sc)
        dados = msg.decode().split(" ")
        if(dados[0].upper() == "UPPER"):
            sendmsg(sc," ".join(dados[1:len(dados)]).upper().encode())
        elif(dados[0].upper() == "LOWER"):
            sendmsg(sc," ".join(dados[1:len(dados)]).lower().encode())
        elif(dados[0].upper() == "LEN"):
            sendmsg(sc,str(len(" ".join(dados[1:len(dados)]))).encode())
        elif(dados[0].upper() == "COUNT"):
            existentes = list(set(" ".join(dados[1:len(dados)])))
            existentes.sort()
            temp = " ".join(dados[1:len(dados)])
            resultado = []
            for i in range(len(existentes)):
                if(existentes[i] != " "):
                    resultado.append(str(temp.count(existentes[i])) + existentes[i])
            sendmsg(sc," ".join(resultado).encode())
        else:
            sendmsg(sc,str(len(dados[1:len(dados)])).encode())

if __name__ == '__main__':
    main()
