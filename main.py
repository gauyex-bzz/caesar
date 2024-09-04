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
