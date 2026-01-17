logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""

print(logo)


alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
    'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
    'u', 'v', 'w', 'x', 'y', 'z'
]

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

encrypted_message = []
decrypted_message = []

def encrypt(original_text, shift_amount):
    for letter in original_text:
        if letter not in alphabet:
            encrypted_message.append(letter)
            continue

        original_position = alphabet.index(letter)
        new_position = (original_position + shift_amount) % len(alphabet)
        encrypted_message.append(alphabet[new_position])

    print(f"Here is the encoded result: {''.join(encrypted_message)}")


def decrypt(original_text, shift_amount):
    for letter in original_text:
        if letter not in alphabet:
            decrypted_message.append(letter)
            continue

        original_position = alphabet.index(letter)
        new_position = (original_position - shift_amount) % len(alphabet)
        decrypted_message.append(alphabet[new_position])

    print(f"Here is the decoded result: {''.join(decrypted_message)}")


def caesar():
    if direction == "encode":
        encrypt(text, shift)
    elif direction == "decode":
        decrypt(text, shift)
    else:
        print("Wrong entry")

caesar()
