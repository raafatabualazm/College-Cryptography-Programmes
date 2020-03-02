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

out_txt = caesar_encrypt("attack", 7)
print(out_txt)