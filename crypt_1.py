from cryptography.fernet import Fernet

def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
    print("Key generated and saved to 'secret.key'.")


def load_key():
    return open("secret.key", "rb").read()


def encrypt_message(message):
    key = load_key()
    cipher = Fernet(key)
    encrypted_message = cipher.encrypt(message.encode())
    return encrypted_message


def decrypt_message(encrypted_message):
    key = load_key()
    cipher = Fernet(key)
    decrypted_message = cipher.decrypt(encrypted_message).decode()
    return decrypted_message

generate_key()


message = input("Enter a message to encrypt: ")
encrypted_msg = encrypt_message(message)
print(f"Encrypted: {encrypted_msg}")

decrypted_msg = decrypt_message(encrypted_msg)
print(f"Decrypted: {decrypted_msg}")
