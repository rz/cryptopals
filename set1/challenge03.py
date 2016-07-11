from itertools import cycle
from util import ascii_score


def fixed_xor(a, b):
    # print(' '*4, 'xor a:', a)
    # print(' '*4, 'xor b:', b)
    xors = [i ^ j for i, j in zip(a, b)]
    return bytes(xors)


if __name__ == '__main__':
    input_str = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
    input_bytes = bytes.fromhex(input_str)
    xors = []
    for c in range(0, 256):
        # unclear what they mean by "single character": either cycling the same
        # character or 0-padded word of the right size
        # these are the possibilities:
        cbs = [
            c.to_bytes(len(input_bytes), 'little'),
            c.to_bytes(len(input_bytes), 'big'),
            bytes([i for i, j in zip(cycle([c]), input_bytes)]),
        ]
        for cb in cbs:
            x = fixed_xor(input_bytes, cb)
            s = ascii_score(x.decode('utf8', errors='replace'))
            xors.append((c, cb, x, s))

    highest_scored = sorted(xors, key=lambda t: t[3], reverse=True)
    for c, cb, x, s in highest_scored[:5]:
        print(c)
        print(cb)
        print(s)
        print(x)
        print('\n\n')

    # lowest_scored = sorted(xors, key=lambda t: t[3], reverse=False)
    # for c, cb, x, s in lowest_scored[:5]:
    #     print(c)
    #     print(cb)
    #     print(s)
    #     print(x)
    #     print('\n\n')
