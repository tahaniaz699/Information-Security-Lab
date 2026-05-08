import hashlib

# --- FUNCTIONS FROM TASK 1 (Must be present) ---
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def multiplicative_inverse(e, phi):
    d, x1, x2, y1, y2 = 0, 0, 1, 1, 0
    temp_phi = phi
    while e > 0:
        temp1, temp2 = divmod(temp_phi, e)
        temp_phi, e = e, temp2
        x, y = x2 - temp1 * x1, y2 - temp1 * y1
        x2, x1, y2, y1 = x1, x, y1, y
    return y2 % phi if temp_phi == 1 else None

def generate_keypair(p, q):
    n = p * q
    phi = (p - 1) * (q - 1)
    e = 65537
    if gcd(e, phi) != 1: e = 3
    d = multiplicative_inverse(e, phi)
    return ((e, n), (d, n))

# --- FUNCTIONS FOR TASK 2 ---

def sign_hash(private_key, message_hash):
    d, n = private_key
    hash_int = int(message_hash, 16) % n
    return pow(hash_int, d, n)

def verify_signature(public_key, message_hash, signature):
    e, n = public_key
    hash_int = int(message_hash, 16) % n
    return pow(signature, e, n) == hash_int

# --- EXECUTION WORKFLOW ---
# 1. Setup Keys
p, q = 101, 103
public_key, private_key = generate_keypair(p, q)

# 2. Original Message
original_message = "Transfer $100 to Alice"
msg_hash = hashlib.sha256(original_message.encode()).hexdigest()
signature = sign_hash(private_key, msg_hash)

print(f"Message: {original_message}")
print(f"Verification: {'SUCCESS' if verify_signature(public_key, msg_hash, signature) else 'FAILED'}")

# 3. Tampered Message
tampered_message = "Transfer $1000 to Alice"
tampered_hash = hashlib.sha256(tampered_message.encode()).hexdigest()

print(f"\nTampered: {tampered_message}")
print(f"Verification: {'SUCCESS' if verify_signature(public_key, tampered_hash, signature) else 'FAILED'}")
