import itertools
import string

import util


def get_likely_keysizes(ciphertext, N, max_keysize, block_count):
    "returns the N most likely key sizes based on lowest normalized edit distance"
    # for each keysize between 2 and 40:
    #   get 1st keysize worth of bytes, 2nd keysize worth of bytes, ... <block count> worth of bytes:
    #      find the average edit distance between the blocks
    #   normalize by dividing by keysize
    #   append to list of (keysize, normalized edit distance) pairs
    # take the N keys with lowest normalized edit distance as likely
    distances = []
    for keysize in range(2, max_keysize + 1):
        blocks = util.chunks(ciphertext, keysize)[:block_count]
        block_pairs = zip(blocks, blocks[1:])
        normalized_distances = [util.hamming_distance(*pair) / keysize for pair in block_pairs]
        average_distance = sum(normalized_distances) / len(normalized_distances)
        distances.append((keysize, average_distance))
    distances = sorted(distances, key=lambda x: x[1])
    return [i for i,j, in distances][:N]


def transpose_and_solve(ciphertext, keysize):
    "returns the most likely key of the given size based on the ascii score of each of the transposed blocks"
    # for each of the likely keysizes:
    #   break the ciphertext into blocks of length keysize
    #   transpose the blocks: make a block with the first byte of every block, one with the 2nd byte of every block and so on
    #   solve each block as if it were single-char XOR: the key that produces the best histogram for a transposed block is that byte of the key
    #   put the key together and use it on the ciphertext
    blocks = util.chunks(ciphertext, keysize)
    transposed_blocks = util.transpose(blocks)
    likely_key = ''
    for block, block_counter in zip(transposed_blocks, itertools.count(1)):
        max_score = 0
        best_guess = ''
        for key_char_guess in string.printable:
            xors = util.fixed_xor(filter(lambda x: x is not None, block), itertools.cycle(bytes(key_char_guess, 'ascii')))
            block_str = ''.join(chr(x) for x in xors)
            score = util.ascii_score(block_str)
            if score >= max_score:
                max_score = score
                best_guess = key_char_guess
        likely_key += best_guess
    return likely_key


def decode(ciphertext, key):
    xord = util.fixed_xor(ciphertext, itertools.cycle(bytes(key, 'ascii')))
    return xord.decode()


if __name__ == '__main__':
    # 0. read the data in
    with open('set1/data/challenge06.txt') as f:
        raw_data = f.read()
    ciphertext = util.base64_to_bytes(raw_data)

    # 1. guess length of key:
    likely_keysizes = get_likely_keysizes(ciphertext, N=4, max_keysize=40, block_count=5)  # parameters picked based on suggestions in the problem

    # 2. break it assuming the keysize is one of the guessed keysizes
    likely_keys = [transpose_and_solve(ciphertext, keysize) for keysize in likely_keysizes]
    decoded = [(key, decode(ciphertext, key)) for key in likely_keys]

    # 3. score the plaintexts by which one looks most like english (ascii) and use the best one
    decoded = sorted(decoded, key=lambda x: util.ascii_score(x[1]), reverse=True)
    key, plaintext = decoded[0]

    print('key:', key)
    print('plaintext:')
    print(plaintext)

