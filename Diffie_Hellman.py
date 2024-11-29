import random

def generate_prime():
    # This is a simplified prime generation.
    # In a real-world scenario, you'd use a more robust method.
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    return random.choice(primes)

def generate_primitive_root(prime):
    # This is a simplified primitive root generation.
    # In practice, you'd use a more sophisticated method.
    for g in range(2, prime):
        if pow(g, prime-1, prime) == 1:
            return g
    return None

def generate_private_key(prime):
    return random.randint(2, prime - 2)

def calculate_public_key(prime, g, private_key):
    return pow(g, private_key, prime)

def calculate_shared_secret(prime, public_key, private_key):
    return pow(public_key, private_key, prime)

# Generate shared parameters
p = generate_prime()
g = generate_primitive_root(p)

print(f"Shared Parameters:")
print(f"Prime (p): {p}")
print(f"Primitive root (g): {g}")

# Generate key pairs for Darshan and Yash
darshan_private = generate_private_key(p)
darshan_public = calculate_public_key(p, g, darshan_private)

yash_private = generate_private_key(p)
yash_public = calculate_public_key(p, g, yash_private)

print("\nDarshan's keys:")
print(f"Private key: {darshan_private}")
print(f"Public key: {darshan_public}")

print("\nYash's keys:")
print(f"Private key: {yash_private}")
print(f"Public key: {yash_public}")

# Calculate shared secrets
darshan_shared_secret = calculate_shared_secret(p, yash_public, darshan_private)
yash_shared_secret = calculate_shared_secret(p, darshan_public, yash_private)

print("\nShared Secrets:")
print(f"Darshan's calculated shared secret: {darshan_shared_secret}")
print(f"Yash's calculated shared secret: {yash_shared_secret}")

if darshan_shared_secret == yash_shared_secret:
    print("\nKey exchange successful! Both parties have the same shared secret.")
else:
    print("\nKey exchange failed. The shared secrets do not match.")

def encrypt_message(message, shared_secret):
    return ''.join([chr(ord(c) ^ shared_secret) for c in message])

def decrypt_message(encrypted_message, shared_secret):
    return ''.join([chr(ord(c) ^ shared_secret) for c in encrypted_message])

# Scenario 1: Darshan sends a message to Yash
sender = "Darshan"
receiver = "Yash"
original_message = "Hello Yash, this is a secret message from Darshan!"

print(f"\nScenario 1: {sender} sends a message to {receiver}")
print(f"Original message: {original_message}")

# Darshan encrypts the message using the shared secret
encrypted_message = encrypt_message(original_message, darshan_shared_secret)
print(f"Encrypted message: {encrypted_message}")

# Yash decrypts the message using the shared secret
decrypted_message = decrypt_message(encrypted_message, yash_shared_secret)
print(f"Decrypted message: {decrypted_message}")

print("\n" + "="*50 + "\n")

# Scenario 2: Yash sends a message to Darshan
sender = "Yash"
receiver = "Darshan"
original_message = "Hi Darshan, I received your message. Here's my reply!"

print(f"Scenario 2: {sender} sends a message to {receiver}")
print(f"Original message: {original_message}")

# Yash encrypts the message using the shared secret
encrypted_message = encrypt_message(original_message, yash_shared_secret)
print(f"Encrypted message: {encrypted_message}")

# Darshan decrypts the message using the shared secret
decrypted_message = decrypt_message(encrypted_message, darshan_shared_secret)
print(f"Decrypted message: {decrypted_message}")



#ALTERNATE CODE

import random

def mod_exp(base, exponent, mod):
    return pow(base, exponent, mod)

p = 23
g = 5

print(f"Publicly shared parameters: p = {p}, g = {g}")

a = random.randint(1, p-1)
b = random.randint(1, p-1)

print(f"Alice's private key: {a}")
print(f"Bob's private key: {b}")

A = mod_exp(g, a, p)
B = mod_exp(g, b, p)

print(f"Alice's public key: {A}")
print(f"Bob's public key: {B}")

shared_secret_alice = mod_exp(B, a, p)
shared_secret_bob = mod_exp(A, b, p)

print(f"Alice's computed shared secret: {shared_secret_alice}")
print(f"Bob's computed shared secret: {shared_secret_bob}")

assert shared_secret_alice == shared_secret_bob, "Key exchange failed!"

print("Shared secret successfully computed!")
