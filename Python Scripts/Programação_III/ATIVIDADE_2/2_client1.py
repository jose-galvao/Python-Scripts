import socket

MAXBYTES = 65535


def find_server(sock):
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    delay = 0.1
    while True:
        sock.sendto(b"DISCOVERY", ('127.255.255.255', 45000))
        sock.settimeout(delay)
        try:
            data, address = sock.recvfrom(MAXBYTES)
        except socket.timeout:
            delay *= 2
            print("Servidor não encontrado!")
        else:
            print("Servidor encontrado em {}".format(address))
            break
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 0)
    sock.settimeout(None)
    return address


def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    address = find_server(sock)
    sock.connect(address)
    while True:
        text = input("Texto/comando: ")
        text = text.upper()
        if text == 'BYE':
            sock.send(b'BYE')
            data = sock.recv(MAXBYTES)
            return 0
        elif text == 'LOWER':
            new_text = input('Texto: ')
            sock.send(b'' + (text + ' ' + new_text).encode())
        elif text == 'LEN':
            new_text = input('Texto: ')
            sock.send(b'' + (text + ' ' + new_text).encode())
        elif text == 'COUNT':
            palavra = input('Diga uma palavra: ')
            letra = input('Qual letra deseja saber a quantidade?: ')
            sock.send(b'' + (text + ' ' + palavra + ' ' + letra).encode())
        elif text == 'WORDS':
            new_text = input('Informe uma frase: ')
            sock.send(b'' + (text + ' ' + new_text).encode())
        else:
            sock.send(b'' + text.encode())
        data = sock.recv(MAXBYTES)
        print("Servidor responde: {}".format(data.decode()))
    sock.close()
    return 0

if __name__ == '__main__':
    main()