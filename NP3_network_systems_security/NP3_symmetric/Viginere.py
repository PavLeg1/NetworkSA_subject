def encrypt_vigenere():
    # Prompt the user to enter the key and plaintext message
    key = input("Enter the key: ")
    message = input("Enter the plaintext message: ")

    # Convert the string key to a numeric array
    key_arr = [ord(c) for c in key]

    # Convert the plaintext message to a numeric array
    msg_arr = [ord(c) for c in message]

    # Pad the key with repeated characters until it is at least as long as the message
    while len(key_arr) < len(msg_arr):
        key_arr += key_arr

    # Encrypt the message using the Vigenere cipher algorithm
    encrypted_arr = []
    for i in range(len(msg_arr)):
        shift = key_arr[i] % 256
        encrypted_arr.append((msg_arr[i] + shift) % 256)

    # Convert the encrypted message back to a string
    encrypted_msg = ''.join([chr(c) for c in encrypted_arr])

    # Return the encrypted message
    print(encrypted_msg)
    return encrypted_msg


def decrypt_vigenere():
    # Prompt the user to enter the key and ciphertext message
    key = input("Enter the key: ")
    ciphertext = input("Enter the ciphertext message: ")

    # Convert the string key to a numeric array
    key_arr = [ord(c) for c in key]

    # Convert the ciphertext message to a numeric array
    cipher_arr = [ord(c) for c in ciphertext]

    # Pad the key with repeated characters until it is at least as long as the ciphertext message
    while len(key_arr) < len(cipher_arr):
        key_arr += key_arr

    # Decrypt the message using the Vigenere cipher algorithm
    decrypted_arr = []
    for i in range(len(cipher_arr)):
        shift = key_arr[i] % 256
        decrypted_arr.append((cipher_arr[i] - shift) % 256)

    # Convert the decrypted message back to a string
    decrypted_msg = ''.join([chr(c) for c in decrypted_arr])

    # Return the decrypted message
    print(decrypted_msg)
    return decrypted_msg


encrypt_vigenere()
decrypt_vigenere()