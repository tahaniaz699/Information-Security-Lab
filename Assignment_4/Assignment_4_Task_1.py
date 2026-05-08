import random
# --- Helper Functions ---
def gcd(a, b):
    """Euclidean algorithm to find the greatest common divisor."""
    while b:
        a, b = b, a % b
    return a

def multiplicative_inverse(e, phi):
    """Extended Euclidean Algorithm to find the modular multiplicative inverse."""
    d = 0
    x1, x2 = 0, 1
    y1, y2 = 1, 0
    temp_phi = phi
    while e > 0:
        temp1 = temp_phi // e
        temp2 = temp_phi - temp1 * e
        temp_phi = e
        e = temp2
        x = x2 - temp1 * x1
        y = y2 - temp1 * y1
        x2, x1 = x1, x
        y2, y1 = y1, y
    if temp_phi == 1:
        return y2 % phi

# --- Core RSA Functions ---
def generate_keypair(p, q):
    # n = p * q
    n = p * q
    # Phi is Euler's totient function
    phi = (p - 1) * (q - 1)
    # Choose an integer e such that e and phi(n) are coprime
    e = 65537  # Common choice for e
    if gcd(e, phi) != 1:
        e = 3  # Fallback for very small primes
    # Use Extended Euclidean Algorithm to generate the private key
    d = multiplicative_inverse(e, phi)
    # Return Public Key (e, n) and Private Key (d, n)
    return ((e, n), (d, n))

def encrypt(public_key, plaintext):
    e, n = public_key
    # Convert characters to numbers and compute: c = m^e mod n
    cipher = [pow(ord(char), e, n) for char in plaintext]
    return cipher

def decrypt(private_key, ciphertext):
    d, n = private_key
    # Compute: m = c^d mod n and convert back to characters
    plain = [chr(pow(char, d, n)) for char in ciphertext]
    return ''.join(plain)

# --- Testing ---
# 1. Choose two small prime numbers
p = 61
q = 53
print(f"Generating keys with p={p} and q={q}...")
public, private = generate_keypair(p, q)
print(f"Public Key: {public}")
print(f"Private Key: {private}")

# 2. Test with a name
message = "M.Taha Niaz"
print(f"\nOriginal Message: {message}")

# 3. Encrypt
encrypted_msg = encrypt(public, message)
print(f"Encrypted (Ciphertext): {encrypted_msg}")

# 4. Decrypt
decrypted_msg = decrypt(private, encrypted_msg)
print(f"Decrypted Message: {decrypted_msg}")
