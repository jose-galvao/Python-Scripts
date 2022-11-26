import socket

MAXBYTES = 65535
def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(('127.0.0.1', 50000))

    while True:
        data, address = sock.recvfrom(MAXBYTES)
        new_data = data.decode()
        num = int(new_data)
        if num > 1:

            for i in range(2, num):

                if (num % i) == 0:
                    new_data = "Não é número primo."
                    break
            else:
                new_data = "É número primo."

        else:
            new_data = "Não é número primo."

        sock.sendto(new_data.encode(), address)
    socket.close()
    return 0
if __name__ == '__main__':
    main()