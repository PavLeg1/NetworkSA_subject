def caesar_encrypt(key, plaintext):
    ciphertext = ''
    for char in plaintext:
        ciphertext += chr((ord(char) + key) % 65536)
    print(ciphertext)
    return ciphertext

def caesar_decrypt(key, ciphertext):
    plaintext = ''
    for char in ciphertext:
        plaintext += chr((ord(char) - key) % 65536)
    print(plaintext)
    return plaintext

caesar_encrypt(2, "wfweafwe")
caesar_decrypt(2, "yhygchyg")