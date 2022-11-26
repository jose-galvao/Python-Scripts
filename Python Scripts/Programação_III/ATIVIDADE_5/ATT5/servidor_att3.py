import socket
import struct
import json
import xmltodict
import zlib


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


def decompress(msg):
    return zlib.decompress(msg)


def toJSON(msg):
    return json.dumps(msg)


def fromJSON(msg):
    return json.loads(msg)


def toCSV(msg):
    csv = ""
    for bruxo, voltas in msg.items():
        csv += ",".join([bruxo] + voltas) + "\n"
    return csv


def fromCSV(msg):
    bruxos = {}
    for l in msg.splitlines():
        ele = l.split(",")
        bruxos[ele[0]] = ele[1:]
    return bruxos


def toXML(msg):
    xml = '<?xml version="1.0" encoding="UTF-8"?><bruxos>'

    for bruxo, voltas in msg.items():
        xml += "<{}>".format(bruxo)
        i = 1
        for v in voltas:
            xml += "<v{0}>{1}</v{0}>".format(i, v)
            i += 1

        xml += "</{}>".format(bruxo)

    xml += "</bruxos>"
    return xml


def fromXML(msg):
    bruxos_t = xmltodict.parse(msg)
    bruxos = {}
    for bruxo, voltas in bruxos_t['bruxos'].items():
        bruxos[bruxo] = list(voltas.values())

    return bruxos


def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(('127.0.0.1', 50000))
    sock.listen(1)

    print("Ouvindo em", sock.getsockname())

    while True:
        sc, sockname = sock.accept()

        feijao = recvmsg(sc).decode()

        feijaosabor = {"tutti-frutti": [toCSV, fromCSV], "vômito": [toXML, fromXML],
                         "marshmallow": [toJSON, fromJSON]}

        bruxos = feijaosabor[feijao][1](decompress(recvmsg(sc)).decode())

        for bruxo, voltas in bruxos.items():
            soma = sum(map(int, bruxos[bruxo]))
            bruxos[bruxo].append(soma)
            bruxos[bruxo] = list(map(str, bruxos[bruxo]))  # opt

        bruxos["__vencedor__"] = [min(bruxos, key=lambda k: bruxos[k][-1])]
        bruxos["__vencedor__"].append(bruxos[bruxos["__vencedor__"][0]][-1])

        sendmsg(sc, compress(feijaosabor[feijao][0](bruxos).encode()))

        sc.close()

    return 0


if __name__ == '__main__':
    main()