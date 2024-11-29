!pip install rsa

import rsa

def generate_keypair(bits=506):
    return rsa.newkeys(bits)

def encrypt_message(message, public_key):
    return rsa.encrypt(message.encode(), public_key)

def decrypt_message(encrypted_message, private_key):
    return rsa.decrypt(encrypted_message, private_key).decode()

# Generate key pairs for Darshan and Yash
darshan_public_key, darshan_private_key = generate_keypair()
yash_public_key, yash_private_key = generate_keypair()

# Print the public and private keys
print("Darshan's Public Key:", darshan_public_key)
print("Darshan's Private Key:", darshan_private_key)
print("Yash's Public Key:", yash_public_key)
print("Yash's Private Key:", yash_private_key)

# Scenario 1: Darshan sends a message to Yash
sender = "Darshan"
receiver = "Yash"
original_message = "Hello Yash, this is a secret message from Darshan!"

print(f"\nScenario 1: {sender} sends a message to {receiver}")
print(f"Original message: {original_message}")

# Darshan encrypts the message using Yash's public key
encrypted_message = encrypt_message(original_message, yash_public_key)
print(f"Encrypted message: {encrypted_message}")

# Yash decrypts the message using his private key
decrypted_message = decrypt_message(encrypted_message, yash_private_key)
print(f"Decrypted message: {decrypted_message}")

print("\n" + "="*50 + "\n")

# Scenario 2: Yash sends a message to Darshan
sender = "Yash"
receiver = "Darshan"
original_message = "Hi Darshan, I received your message. Here's my reply!"

print(f"Scenario 2: {sender} sends a message to {receiver}")
print(f"Original message: {original_message}")

# Yash encrypts the message using Darshan's public key
encrypted_message = encrypt_message(original_message, darshan_public_key)
print(f"Encrypted message: {encrypted_message}")

# Darshan decrypts the message using her private key
decrypted_message = decrypt_message(encrypted_message, darshan_private_key)
print(f"Decrypted message: {decrypted_message}")


#ALTERNATE CODE

import random

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def modular_inverse(e, phi):
    return pow(e, -1, phi)

def generate_keys():
    # Two random prime numbers
    p = 61
    q = 53
    n = p * q
    phi = (p - 1) * (q - 1)

    # Choose e such that 1 < e < phi and gcd(e, phi) = 1
    e = random.randrange(1, phi)
    while gcd(e, phi) != 1:
        e = random.randrange(1, phi)

    d = modular_inverse(e, phi)

    public_key = (e, n)
    private_key = (d, n)

    return public_key, private_key

def encrypt(public_key, plaintext):
    e, n = public_key
    ciphertext = [(ord(char) ** e) % n for char in plaintext]
    return ciphertext

def decrypt(private_key, ciphertext):
    d, n = private_key
    plaintext = ''.join([chr((char ** d) % n) for char in ciphertext])
    return plaintext

public_key, private_key = generate_keys()
print("Public Key:", public_key)
print("Private Key:", private_key)

message = "HELLO"
print("\nOriginal Message:", message)

encrypted_message = encrypt(public_key, message)
print("\nEncrypted Message:", encrypted_message)

decrypted_message = decrypt(private_key, encrypted_message)
print("\nDecrypted Message:", decrypted_message)

