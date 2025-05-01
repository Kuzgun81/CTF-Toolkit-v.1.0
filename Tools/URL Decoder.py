import urllib.parse

def url_decoder():
    print("URL Decoder")
    url_encoded = input("Şifreli URL'yi girin (örneğin: Hello%20World): ")
    
    try:
        decoded_url = urllib.parse.unquote(url_encoded)
        print("Çözümlenen URL:", decoded_url)
    except Exception as e:
        print("Hata: URL çözümleme sırasında bir hata oluştu.")
        print(f"Detay: {e}")
