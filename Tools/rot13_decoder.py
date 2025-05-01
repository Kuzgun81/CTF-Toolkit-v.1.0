def rot13_decoder():
    print("ROT13 Decoder")
    text = input("ROT13 ile şifrelenmiş metni girin: ")
    decoded = ""

    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            decoded += chr((ord(char) - base + 13) % 26 + base)
        else:
            decoded += char

    print("Çözümlenen metin:", decoded)

