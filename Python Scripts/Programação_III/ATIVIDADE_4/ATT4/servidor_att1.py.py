import socket
import pickle


def recvall(sock):
    data = b""
    while True:
        more = sock.recv(1024)

        if not more:
            break
        data += more
    return data

def max(temp):
    maior={"maxima": 0, "minima": 0, "cidade": ""}
    for i in temp:
        if(maior['maxima']<i['maxima']):
            maior=i

    return maior

def min(temp1):
    menor=temp1[0]

    for i in temp1:
        if(menor['maxima']>i['maxima']):
            menor=i
    return menor







def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(('127.0.0.1', 50000))
    sock.listen(1)

    print("Ouvindo em", sock.getsockname())
    banco_dados=[]
    while True:
        sc, sockname = sock.accept()
        sc.shutdown(socket.SHUT_WR)
        msg = recvall(sc)
        banco_dados.append(pickle.loads(msg))
        max(banco_dados)
        maior= max(banco_dados)
        menor= min(banco_dados)

        print(banco_dados)

        print("Maior cidade é:"+str(maior['cidade'])+" Temperatura de: "+ str(maior['maxima']))
        print("Menor cidade é:"+str(menor['cidade'])+" Temperatura de: "+ str(menor['maxima']))

        sc.close()

    return 0

if __name__ == '__main__':
    print("Servidor ligado")
    main()