def caesar_decoder():
    print("Caesar Decoder")
    ciphertext = input("Şifreli metni girin: ")

    print("\nOlası çözümler:")
    for shift in range(1, 26):
        decoded = ''
        for char in ciphertext:
            if char.isalpha():
                offset = 65 if char.isupper() else 97
                decoded += chr((ord(char) - offset - shift) % 26 + offset)
            else:
                decoded += char
        print(f"{shift:2}: {decoded}")

# Doğrudan çalıştırma kodu
if __name__ == "__main__":
    caesar_decoder()
