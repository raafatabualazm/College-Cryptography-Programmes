import sys

inverses = dict()
inverses[1] = 1
inverses[3] = 9
inverses[5] = 21
inverses[7] = 15
inverses[9] = 3
inverses[11] = 19
inverses[15] = 7
inverses[17] = 23
inverses[19] = 11
inverses[21] = 15
inverses[23] = 17
inverses[25] = 25

def caesar_encrypt(plain_text, b):
    cipher_text = ""
    b = b % 26
    for x in range(len(plain_text)):
        pc = ord(plain_text[x]) - ord('a')
        cc = (pc + b) % 26
        cc = cc + ord('a')
        cc = chr(cc)
        cipher_text += cc
    return cipher_text


def caesar_decrypt(cipher_text, b):
    plain_text = ""
    b = b % 26
    b = (b != 0)*(26 - b)
    for x in range(len(cipher_text)):
        cc = ord(cipher_text[x]) - ord('a')
        pc = (cc + b) % 26
        pc = pc + ord('a')
        pc = chr(pc)
        plain_text += pc
    return plain_text


def vigenere_encrypt(plain_text, bs):
    cipher_text = ""
    i = 0
    for x in range(len(plain_text)):
        b = bs[i] - ord('a')
        pc = ord(plain_text[x]) - ord('a')
        cc = (pc + b) % 26
        cc = cc + ord('a')
        cc = chr(cc)
        cipher_text += cc
        i = (i + 1) % len(bs)
    return  cipher_text

def vigenere_decrypt(cipher_text, bs):
    plain_text = ""
    i = 0
    for x in range(len(cipher_text)):
        b = bs[i] - ord('a')
        b = (b != 0) * (26 - b)
        cc = ord(cipher_text[x]) - ord('a')
        pc = (cc + b) % 26
        pc = pc + ord('a')
        pc = chr(pc)
        plain_text += pc
        i = (i + 1) % len(bs)
    return plain_text

def affine_encrypt(plain_text, a, b):
    cipher_text = ""
    a = a % 26
    b = b % 26
    for x in range(len(plain_text)):
        pc = ord(plain_text[x]) - ord('a')
        cc = ((pc * a) % 26 + b) % 26
        cc = cc + ord('a')
        cc = chr(cc)
        cipher_text += cc
    return cipher_text

def affine_decrypt(cipher_text, a, b):
    plain_text = ""
    a = a % 26
    b = b % 26
    b = (b != 0) * (26 - b)
    a = inverses[a]
    for x in range(len(cipher_text)):
        cc = ord(cipher_text[x]) - ord('a')
        pc = (a * (cc + b) % 26) % 26
        pc = pc + ord('a')
        pc = chr(pc)
        plain_text += pc
    return plain_text


fhr = open(sys.argv[3], 'r')
fhw = open(sys.argv[4], 'w')
in_txt = fhr.read()
out_txt = ""
if sys.argv[1] == "shift":
    a = int(sys.argv[5])
    print(a)
    if sys.argv[2] == "decrypt":
        out_txt = caesar_decrypt(in_txt, a)
        fhw.write(out_txt)
    elif sys.argv[2] == "encrypt":
        out_txt = caesar_encrypt(in_txt, a)
        fhw.write(out_txt)

elif sys.argv[1] == "affine":
    a = int(sys.argv[5])
    b = int(sys.argv[6])
    if sys.argv[2] == "decrypt":
        out_txt = affine_decrypt(in_txt, a, b)
        fhw.write(out_txt)
    elif sys.argv[2] == "encrypt":
        out_txt = affine_encrypt(in_txt, a, b)
        fhw.write(out_txt)

elif sys.argv[1] == "vigenere":
    a = sys.argv[5]
    if sys.argv[2] == "decrypt":
        out_txt = vigenere_decrypt(in_txt, a)
        fhw.write(out_txt)
    elif sys.argv[2] == "encrypt":
        out_txt = vigenere_encrypt(in_txt, a)
        fhw.write(out_txt)
