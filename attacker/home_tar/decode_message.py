def bits_to_message(bits):
    # Chia chuỗi bit thành các byte (8 bit) và chuyển đổi mỗi byte thành ký tự
    message = ''.join(chr(int(bits[i:i+8], 2)) for i in range(0, len(bits), 8))
    return message

bits = input("Enter the decoded bit string: ")
decoded_message = bits_to_message(bits)
print(f"Decoded message: {decoded_message}")

