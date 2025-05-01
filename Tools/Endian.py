def endian_converter():
    print("Endian Converter")
    binary_string = input("Binary string'i girin (örnek: 0100000101000010): ")
    

    little_endian = ''.join(reversed([binary_string[i:i+8] for i in range(0, len(binary_string), 8)]))
    print("Little Endian formatı:", little_endian)

