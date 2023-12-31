# -*- coding: utf-8 -*-
"""k200428 Nausherwan baig.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Hk_73DMH9GsrlUfeXjfXKk4AUSK3Vqec

**RSA** **ALGORITHM**
"""

# Function to calculate the greatest common divisor (GCD) of two numbers a and b
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Function to calculate the modular inverse of a number 'a' with the number modulo 'm'
def mod_inverse(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

# Function to generate an RSA key pair given prime numbers 'p', 'q', and 'e'
def generate_rsa_keypair(p, q, e):
    n = p * q
    phi = (p - 1) * (q - 1)

    # Check if 'e' is coprime with 'phi'
    if gcd(e, phi) != 1:
        raise ValueError("e is not coprime with phi.recalculate and enter a different value")

    # Calculate d
    d = mod_inverse(e, phi)

    # Return the public and private keys
    return {"public_key": (e, n), "private_key": (d, n)}

# Function to encrypt a numeric value using the RSA public key
def rsa_encrypt(public_key, numeric_value):
    e, n = public_key
    ciphertext = pow(numeric_value, e, n)
    return ciphertext

# Function to decrypt a ciphertext using the RSA private key
def rsa_decrypt(private_key, ciphertext):
    d, n = private_key
    decrypted_value = pow(ciphertext, d, n)
    return decrypted_value

# Input values
p = int(input("Enter a prime number p: "))
q = int(input("Enter a prime number q: "))
e = int(input("Enter a public exponent e: "))

# Generate RSA key pair
rsa_keys = generate_rsa_keypair(p, q, e)

# Display the RSA keys
print("\n RSA algorithm Public Key (e, n):", rsa_keys["public_key"])
print("\n\n RSA algorithm Private Key (d, n):", rsa_keys["private_key"])

# Input numeric value to encrypt
numeric_value = int(input("\nEnter a value for encryption: "))

# Encrypt the numeric value using the public key
encrypted_value = rsa_encrypt(rsa_keys["public_key"], numeric_value)
print("Encrypted value:", encrypted_value)

# Decrypt the ciphertext using the private key
decrypted_value = rsa_decrypt(rsa_keys["private_key"], encrypted_value)
print("Decrypted value:", decrypted_value)