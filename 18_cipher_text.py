alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(plain_text, shift_amount):
    cipher_text = ""
    for letter in plain_text:
        position=alphabet.index(letter)
        print(f"Position {position}")
        new_postion=position+shift_amount
        print(f"Position {new_postion}")
        if new_postion>25:
            for i in range(25,30):
                new_letter=alphabet
        new_letter=alphabet[new_postion]
        cipher_text+=new_letter
    print(f"The encoded text is {cipher_text}")




encrypt(text,shift)