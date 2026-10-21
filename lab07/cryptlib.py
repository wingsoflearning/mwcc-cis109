#encrypt(message, shift) : This function will use Caesar Cypher encryption to shift each message character by the specified number of positions in the alphabet.
#decrypt(message, shift) : This function simply calls the encrypt function, with a minus in front of the second parameter to reverse the shift of the Caesar Cypher.

def encrypt(message, shift):
    encrypted_message = ""

    for char in message:
        if char.isalpha():
            start = 65 if char.isupper() else 97
            new_char = chr((ord(char) - start + shift) % 26 + start)
            encrypted_message += new_char
        else:
            encrypted_message += char

    return encrypted_message

def decrypt(message, shift):
    return encrypt(message, -shift)
