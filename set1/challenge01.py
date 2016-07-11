# keeping imports in the functions to make it clear what's needed for each
# implementation.


# my original solution:
# def hex_to_base64(input_str):
#     import binascii

#     bytes = binascii.unhexlify(input_str)
#     base64_bytes = binascii.b2a_base64(bytes)[:-1]  # this adds an extra new line at the end
#     return base64_bytes.decode('ascii')  # so that it is safe to print


# alternative version without the [:-1] thing
# def hex_to_base64(input_str):
#     import base64
#     import binascii
#     bytes = binascii.unhexlify(input_str)
#     base64_bytes = base64.b64encode(bytes)
#     return base64_bytes.decode('ascii')


# yet anoter alternative version, which seems the most pythonic
def hex_to_base64(input_str):
    import base64

    bs = bytes.fromhex(input_str)
    return base64.b64encode(bs).decode('utf8')


if __name__ == '__main__':
    input_str = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
    expected_str = 'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'
    result = hex_to_base64(input_str)
    print(result)
    if result != expected_str:
        print('NOT RIGHT')
