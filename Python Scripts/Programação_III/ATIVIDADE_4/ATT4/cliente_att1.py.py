import socket
import pickle


def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('127.0.0.1', 50000))
    sock.shutdown(socket.SHUT_RD)
    dic = {"maxima": 0, "minima": 0, "cidade": ""}

    print("Temperatura maxima:")
    maxima=int(input())
    dic["maxima"]=maxima
    print("Temperatura minima:")
    minima=int(input())
    dic["minima"]=minima
    print("Que cidade está com essa temperatura?:")
    cidade = str(input())
    dic["cidade"] = cidade
    print(dic)

    sock.sendall(pickle.dumps(dic))
    sock.close()

    return 0

if __name__ == '__main__':
    print("Cliente ligado")
    main()