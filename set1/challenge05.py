import binascii
from itertools import cycle, zip_longest


def fixed_xor(a, b):
    # print(' '*4, 'xor a:', a)
    # print(' '*4, 'xor b:', b)
    xors = [i ^ j for i, j in zip(a, b)]
    return bytes(xors)


def encrypt(in_str, key):
    input_bytes = bytes(s, 'utf8')
    key_bytes = bytes(key, 'utf8')
    xord = fixed_xor(input_bytes, cycle(key_bytes))
    xord = binascii.hexlify(xord).decode()
    return xord

if __name__ == '__main__':
    input_strs = [
        "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal",
        "Burning 'em, if you ain't quick and nimble\n",
        "I go crazy when I hear a cymbal",
    ]
    expected_outs = [
        '0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f',
        '0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272',
        'a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f',
    ]
    key = 'ICE'

    for s, expected in zip_longest(input_strs, expected_outs):
        xord = encrypt(s, key)
        print('in:   ', s)
        print('xord: ', xord)
        if expected is not None and xord != expected:
            print('ex:   ', expected)
            print('NOT RIGHT!!')
        print('-'*20)

    print('\n\n')

    input_strs = [
        'hello world',
        'abcdefghijk',
        'a',
        'b',
        'c',
        'ab',
        'abc',
        'abcd',
        'abcde',
        'bcd',
        'cde',
        '$up3r$3cr337',
        '_dovenull:*:227:227:Dovecot Authentication:/var/empty:/usr/bin/false',
        'ICE'*10,
        'ICE'*10+'x',
        'ICE'*10+'xx',
        'IC'*10,
        '\x00'*20,
    ]
    for s in input_strs:
        xord = encrypt(s, key)
        print('in           : ', s)
        print('in (bytes)   : ', bytes(s, 'utf8'))
        print('xord         : ', xord)
        print('xord (nohex) :', binascii.unhexlify(xord))
        print('-'*20)
