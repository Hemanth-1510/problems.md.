def caesar_cipher(message, shift, mode='encode'):
    shift = shift % 26
    if mode == 'decode':
        shift = -shift
    return ''.join(
        chr((ord(c) - base + shift) % 26 + base) if c.isalpha() else c
        for c in message
        for base in [ord('A') if c.isupper() else ord('a')] if c.isalpha()
    )

# Input
message = input().strip()
shift = int(input())
mode = input().strip()  # 'encode' or 'decode'
print(caesar_cipher(message, shift, mode))
