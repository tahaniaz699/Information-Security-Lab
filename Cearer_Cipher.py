def caesar_encrypt(text, shift):
    result = ""

    for char in text:
        # Check if character is uppercase letter
        if char.isupper():
            new_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            result += new_char

        # Check if character is lowercase letter
        elif char.islower():
            new_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            result += new_char

        # If not a letter (space, number, symbol), keep it same
        else:
            result += char

    return result

def caesar_decrypt(ciphertext, shift):
    return caesar_encrypt(ciphertext, -shift)

# ---- Main Program ----
message = input("Enter your message: ")
shift_value = int(input("Enter shift value: "))

encrypted = caesar_encrypt(message, shift_value)
print("Encrypted Message:", encrypted)

decrypted = caesar_decrypt(encrypted, shift_value)
print("Decrypted Message:", decrypted)
