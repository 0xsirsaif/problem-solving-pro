def cyclic_shitf_hash_code(s: str):
    # to limit the length to 32-bit. mask = 0b11111111111111111111111111111111
    mask = (1 << 32) - 1
    h = 0
    for character in s:
        # cyclic-shift. << higher precedence than &
        h = (h << 5 & mask) | (h >> 27)
        # append charcter unicode to h.
        h += ord(character)
    return bin(h)


print(cyclic_shitf_hash_code("mohamed"))
