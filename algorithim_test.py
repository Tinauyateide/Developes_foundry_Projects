def encrypt(message, key): 
    encrypted_message = ""
    for char in message:
        if 'a' <= char.lower() <= 'z':
            my_val = ord('a') if char.islower() else ord('A')
            shift_char = chr((ord(char) - my_val + key) % 26 + my_val)
            encrypted_message += shift_char    
        else:
            encrypted_message += char
    return encrypted_message

def decrypt(message, key):
    return encrypt(message, -key)


my_message = input("Enter a message to encrypt: ")
my_key = int(input("Enter a number to shift the letters: "))

cipher_text = encrypt(my_message, my_key)
print(f"Encrypted message: {cipher_text}")

decrypted_text = decrypt(cipher_text, my_key)
print(f"Decrypted message: {decrypted_text}")