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

def somar(num1,num2):
    return num1+num2
def multi(num1,num2):
    return num1*num2
def div(num1,num2):
    return num1/num2
def sub(num1,num2):
    return num1-num2
def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(('127.0.0.1', 50000))
    sock.listen(1)

    print("Ouvindo em", sock.getsockname())

    while True:
        sc, sockname = sock.accept()

        msg = recvall(sc, 9)
        nums = struct.unpack("!iis", msg)
        operacao=0
        if(nums[2]==b'*'):
            operacao= multi(nums[0], nums[1])

        elif(nums[2]==b'+'):
            operacao= somar(nums[0], nums[1])
        elif (nums[2] == b'-'):
            operacao = sub(nums[0], nums[1])
        elif (nums[2] == b'/'):
            operacao = div(nums[0], nums[1])

        sc.sendall(struct.pack("!i", operacao))

        sc.close()

    return 0

if __name__ == '__main__':
    print("Servidor ligado")
    main()