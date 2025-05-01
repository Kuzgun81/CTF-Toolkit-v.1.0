def hex_to_ascii():
    print("Hex to ASCII")
    hex_string = input("Hexadecimal string'i girin (örnek: 68656c6c6f): ")
    
    try:
        
        ascii_string = bytes.fromhex(hex_string).decode('utf-8')
        print("ASCII metin:", ascii_string)
    except Exception as e:
        print("Hata: Geçersiz Hexadecimal string")
        print(f"Detay: {e}")



