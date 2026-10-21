#1. Write a Python module named caesar.py, which will take the following command-line arguments:
#-d : Decrypt the message.
#-e : Encrypt the message.
#-m : The message to encrypt/decrypt.
#2. Use the argparse library to parse these options.
#Ensure each option is properly configured (required=True/False, etc.) and has appropriate help text.
#Ensure you're handling the scenario of what happens if the user attempts to pass in both -d and -e options.
#3. Use a from-import statement to import the custom encrypt/decrypt functions you wrote earlier.
#4. Use the imported encrypt/decrypt functions with the appropriate command-line option.

import argparse
from cryptlib import encrypt, decrypt

def main():
    parser = argparse.ArgumentParser(description="Caesar Cipher Command-Line Utility")
    
    # Require a message to process
    parser.add_argument("-m", "--message", required=True, help="The message to encrypt/decrypt.")
    
    # Make exclusive group so -e and -d cannot be used together
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-e", "--encrypt", type=int, metavar="SHIFT", help="Encrypt the message with the specified shift integer.")
    group.add_argument("-d", "--decrypt", type=int, metavar="SHIFT", help="Decrypt the message with the specified shift integer.")
    
    args = parser.parse_args()
    
    if args.encrypt is not None:
        result = encrypt(args.message, args.encrypt)
        print(f"Encrypted Message: {result}")
    elif args.decrypt is not None:
        result = decrypt(args.message, args.decrypt)
        print(f"Decrypted Message: {result}")

if __name__ == "__main__":
    main()