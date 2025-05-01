import os
import time

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def ascii_logo():
    logo = r'''
   ____  _______ ______    __    __  .______     ______   .___________. __    ______   .______      
  / __ \ \_   __ \____ \  |  |  |  | |   _  \   /  __  \  |           ||  |  /  __  \  |   _  \     
 | |  | | |    |  |  |_> > |  |__|  | |  |_)  | |  |  |  | `---|  |----`|  | |  |  |  | |  |_)  |    
 | |  | | |    |  |   __/  |   __   | |   ___/  |  |  |  |     |  |     |  | |  |  |  | |   ___/     
 | |__| | |____|  |__|     |  |  |  | |  |      |  `--'  |     |  |     |  | |  `--'  | |  |         
  \____/       |__|       |__|  |__| | _|       \______/      |__|     |__|  \______/  | _|         
                                                                                                   
    '''
    print(logo)

def menu():
    while True:
        clear()
        ascii_logo()
        print("CTF Help Tool Pack v1.0")
        print("="*40)
        print("[1] Base64 Decoder")
        print("[2] Hex to ASCII")
        print("[3] ROT13 / Caesar Çözücü")
        print("[4] XOR Decoder")
        print("[5] URL Decode")
        print("[6] Reverse String / Endian")
        print("[7] Stego Tools (geliştirilecek)")
        print("[0] Çıkış")
        print("="*40)

        choice = input("Bir seçenek gir: ")

        if choice == '1':
            print("Base64 decoder çalışıyor...")
            time.sleep(1)
            
        elif choice == '2':
            print("Hex çözücü çalışıyor...")
            time.sleep(1)
           
        elif choice == '3':
            print("Caesar çözücü çalışıyor...")
            time.sleep(1)
           
        elif choice == '4':
            print("XOR çözücü çalışıyor...")
            time.sleep(1)
            
        elif choice == '5':
            print("URL decode çalışıyor...")
            time.sleep(1)
            
        elif choice == '6':
            print("Reverse tool çalışıyor...")
            time.sleep(1)
          
        elif choice == '7':
            print("Stego tools yakında...")
            time.sleep(1)
        elif choice == '0':
            print("Çıkış yapılıyor...")
            break
        else:
            print("Try Again.")
            time.sleep(1)

if __name__ == "__main__":
    menu()

