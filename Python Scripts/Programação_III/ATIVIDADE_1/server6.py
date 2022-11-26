import socket
import datetime

MAXBYTES = 65535
def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(('127.0.0.1', 50002))
    while True:
        agora = datetime.datetime.now()
        data, address = sock.recvfrom(MAXBYTES)
        new_data = data.decode().upper()

        if new_data == 'DATA':
            new_data = 'A data de hoje é '+ agora.strftime('%m/%d/%Y')
        elif new_data == 'DIA':
            new_data = 'O dia de hoje é '+ agora.strftime('%d')
        elif new_data == 'MÊS':
            new_data = 'Nós estamos no mês ' + agora.strftime('%m')
        elif new_data == 'ANO':
            new_data = 'Nós estamos no ano '+ agora.strftime('%Y')
        elif new_data == 'HORA':
            new_data = 'Agora são ' + agora.strftime('%H:%M:%S')
        else:
            break
        sock.sendto(new_data.encode(), address)
    socket.close()
    return 0
if __name__ == '__main__':
    main()