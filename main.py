def encrypt():
    text = input("Geben Sie den Text ein, den Sie verschlüsseln möchten: ")
    shift = int(input("Geben Sie die Verschiebung (Schlüssel) ein (- zum entschlüsseln): "))

    result = ""

    for char in text:
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char

    print("Verschlüsselter Text:", result)


def decrypt():
    text = input("Geben Sie den Text ein, den Sie entschlüsseln möchten: ")
    shift = int(input("Geben Sie die Verschiebung (Schlüssel) ein (- zum entschlüsseln): "))

    result = ""

    for char in text:
        if char.isupper():
            result += chr((ord(char) - shift - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) - shift - 97) % 26 + 97)
        else:
            result += char

    print("Entschlüsselter Text:", result)


if __name__ == "__main__":
    en_or_decrypt = input("Wollen Sie verschlüsseln oder entschlüsseln? (v/e): ")
    if en_or_decrypt == "v":
        encrypt()
    elif en_or_decrypt == "e":
        decrypt()
    else:
        print("Ungültige Eingabe!")
