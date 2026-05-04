# Parameters for y^2 = x^3 + 2x + 2 (mod 17)
P = 17
A = 2
B = 2


def point_add(P1, P2, p, a):
    if P1 is None: return P2
    if P2 is None: return P1
    x1, y1 = P1
    x2, y2 = P2

    if x1 == x2 and y1 != y2: return None  # Point at infinity

    # Calculate Slope (m)
    if x1 == x2:  # Point Doubling
        m = (3 * x1 ** 2 + a) * pow(2 * y1, -1, p)
    else:  # Point Addition
        m = (y2 - y1) * pow(x2 - x1, -1, p)

    m %= p
    x3 = (m ** 2 - x1 - x2) % p
    y3 = (m * (x1 - x3) - y1) % p
    return (x3, y3)


def scalar_mult(k, point, p, a):
    result = None
    addend = point
    while k:
        if k & 1: result = point_add(result, addend, p, a)
        addend = point_add(addend, addend, p, a)
        k >>= 1
    return result


# --- ECC Key Gen & Simplified ElGamal ---
G = (5, 1)  # Generator point on our curve
priv_key = 7
pub_key = scalar_mult(priv_key, G, P, A)  # Public Key B = dG

# Encryption of message M (point on curve)
M = (9, 1)  # Let's assume our message maps to this point
k = 3  # Ephemeral random key
C1 = scalar_mult(k, G, P, A)
C2 = point_add(M, scalar_mult(k, pub_key, P, A), P, A)

# Decryption: M = C2 - (priv_key * C1)
shared_secret = scalar_mult(priv_key, C1, P, A)
neg_shared_secret = (shared_secret[0], (-shared_secret[1]) % P)
decrypted_M = point_add(C2, neg_shared_secret, P, A)

print(f"Original Message Point: {M}")
print(f"Decrypted Message Point: {decrypted_M}")