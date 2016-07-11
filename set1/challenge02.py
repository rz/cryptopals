# keeping imports in functions to make dependencies clear


# original solution:
# def fixed_xor(a, b):
#     xors = [i ^ j for i, j in zip(a, b)]
#     xors_hex = [hex(i)[2:] for i in xors]  # yuck, this is ugly
#     result_str = ''.join(xors_hex)
#     return result_str

def fixed_xor(a, b):
    import binascii

    xord = bytes([i ^ j for i, j in zip(a, b)])
    return binascii.hexlify(xord).decode('utf8')


if __name__ == '__main__':
    # inputs need to be hex-decoded
    input_str1 = '1c0111001f010100061a024b53535009181c'
    a = bytes.fromhex(input_str1)

    input_str2 = '686974207468652062756c6c277320657965'
    b = bytes.fromhex(input_str2)

    result = fixed_xor(a, b)
    print(result)

    expected = '746865206b696420646f6e277420706c6179'
    if result != expected:
        print('NOT RIGHT')
