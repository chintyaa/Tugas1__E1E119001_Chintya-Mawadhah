def enkripsi(plaintext, key):
    encoded = []

    for i in range(len(plaintext)):
        xor = ord(plaintext[i]) ^ ord(key[i % len(key)])
        encoded.append(chr(xor))

    return ''.join(encoded)

def dekripsi(chipertext, key):
    return enkripsi(chipertext, key)

def main():
    plaintext = str(input("Masukan plaintext: "))
    key = 'CCC'

    print("Plaintext: ", plaintext)
    print("Enkripsi: ", enkripsi(plaintext, key))
    chipertext = str(input("Masukan chipertext: "))
    key = "CCC"

    print("Chipertext: ", chipertext)
    print("Dekripsi: ", dekripsi(chipertext, key))

main()