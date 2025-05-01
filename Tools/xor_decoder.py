def xor_decoder():
    print("XOR Decoder")
    ciphertext = input("XOR ile şifrelenmiş metni girin: ")
    key = input("XOR anahtarını girin: ")

    try:
        
        decoded = ''.join([chr(ord(c) ^ ord(key)) for c in ciphertext])
        print("Çözümlenen metin:", decoded)
    except Exception as e:
        print("Hata: XOR çözümleme sırasında bir hata oluştu.")
        print(f"Detay: {e}")
