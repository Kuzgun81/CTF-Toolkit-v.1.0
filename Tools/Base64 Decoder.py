import base64

def base64_decoder():
    print("Base64 Decoder")
    encoded_string = input("Base64 ile şifrelenmiş metni girin: ")
    
    try:
        decoded_bytes = base64.b64decode(encoded_string)
        decoded_string = decoded_bytes.decode('utf-8')
        print("Çözümlenen metin:", decoded_string)                                           
    except Exception as e:
        print("Hata: Geçersiz Base64 kodu")
        print(f"Detay: {e}")

