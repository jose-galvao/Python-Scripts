import socket
MAXBYTES = 65535

def main():
    sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    sock.bind(('0.0.0.0',45000))
    while True:
        data, address = sock.recvfrom(MAXBYTES)
        values = data.split()

        if values[0] == b'LOWER':
            sock.sendto(values[1].lower(), address)
        elif values[0] == b'LEN':
            sock.sendto(str(len(values[1])).encode(), address)
        elif values[0] == b'COUNT':
            values[1].count(values[2])
            sock.sendto(str(values[1].count(values[2])).encode(), address)
        elif values[0] == b'WORDS':
            sock.sendto(str(len(values) - 1).encode(), address)
        elif data == b'BYE':
            sock.sendto(b'BYE',address)
            break
        else:
            sock.sendto(b'' + data,address)
    sock.close()
    return 0

if __name__ == '__main__':
    main()