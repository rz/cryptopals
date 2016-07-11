from itertools import cycle
from util import ascii_score


def fixed_xor(a, b):
    # print(' '*4, 'xor a:', a)
    # print(' '*4, 'xor b:', b)
    xors = [i ^ j for i, j in zip(a, b)]
    return bytes(xors)


if __name__ == '__main__':
    with open('set1/data/challenge04.txt') as f:
        lines = [l.strip() for l in f.readlines()]

    results = []
    for line in lines:
        line_bytes = bytes.fromhex(line)
        for c in range(0, 256):
            char_bytes = bytes([i for i, j in zip(cycle([c]), line_bytes)])
            xor = fixed_xor(line_bytes, char_bytes)
            score = ascii_score(xor.decode('utf8', errors='replace'))
            results.append((c, line, line_bytes, xor, score))
    results = sorted(results, key=lambda t:t[4], reverse=True)
    for r in results[:5]:
        print(r)
