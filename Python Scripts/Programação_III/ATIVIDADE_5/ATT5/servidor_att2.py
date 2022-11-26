import socket
import zlib
import json
import struct
import ast
import xml.etree.ElementTree
import xmltodict


def convert(xml_file, xml_attribs=True):
    with open(xml_file, "rb") as f:
        d = xmltodict.parse(f, xml_attribs=xml_attribs)
        return d


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


def stringToDicionario(dicionario):
    return ast.literal_eval(dicionario)


def tagsDosAlunos(nome):
    et = xml.etree.ElementTree.parse('notas.xml')
    dicionario = nome
    for i in nome:
        new_tag = xml.etree.ElementTree.SubElement(et.getroot(), i)
        print(i)
        new_tag.attrib['n1'] = dicionario[i][0]
        new_tag.attrib['n2'] = dicionario[i][1]
        new_tag.attrib['n3'] = dicionario[i][2]
        et.write('notas.xml')


def mediaCalcula(n1, n2, n3):
    return float(n1) + float(n2) + float(n3)


def retornarDadosDicionario():
    informacao = "\n"

    notas = convert('notas.xml')
    str_xml = xmltodict.unparse(notas)
    n = dict(xmltodict.parse(str_xml))
    chaves = dict(n['alunos'])
    elemento = len(chaves)
    cont = 0
    for i in chaves:

        if (cont == 0 or (elemento - 1) == cont):
            numero = dict(chaves[i])
            informacao += "O aluno " + i + " obteve a média " + str(
                mediaCalcula(numero['@n1'], numero['@n2'], numero['@n3']))

        else:
            numero = dict(chaves)[i]
            numero = dict(numero[0])
            informacao += "||" + "O aluno " + i + " obteve a média " + str(
                mediaCalcula(numero['@n1'], numero['@n2'], numero['@n3']))

        cont += 1

    return informacao


def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(('127.0.0.1', 50000))
    sock.listen(1)

    print("Ouvindo em", sock.getsockname())

    while True:
        sc, sockname = sock.accept()
        notas = descompress(recvmsg(sc)).decode()
        dicionario = stringToDicionario(notas)
        tagsDosAlunos(dicionario)

        print(retornarDadosDicionario())

        sendmsg(sc, compress(str(retornarDadosDicionario()).encode()))

        sc.close()

    return 0


if _name_ == '_main_':
    main()