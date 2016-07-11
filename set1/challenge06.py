import itertools
import string

import util


def get_blocks(_bytes, size):
    return [_bytes[i*size:(i+1)*size] for i in range(block_count)]


def get_distances(_bytes, block_count=2):
    distances = []
    for keysize in range(2, 41):
        blocks = util.chunks(_bytes, keysize)[:block_count]
        block_pairs = zip(blocks, blocks[1:])
        normalized_distances = [util.hamming_distance(*pair) / keysize for pair in block_pairs]
        average_distance = sum(normalized_distances) / len(normalized_distances)
        distances.append((keysize, average_distance))
    distances = sorted(distances, key=lambda x: x[1])
    return distances


if __name__ == '__main__':
    with open('set1/data/challenge06.txt') as f:
        b64_bytes = util.base64_to_bytes(f.read())

    # alphabet = string.ascii_letters + string.digits
    # for key_size in range(1, 6):
    #     possible_keys = itertools.combinations_with_replacement(alphabet, key_size)
    #     key_scores = []
    #     for key_tuple in possible_keys:
    #         key = bytes(''.join(key_tuple), 'ascii')
    #         xord = util.fixed_xor(b64_bytes, itertools.cycle(key)).decode(errors='replace')
    #         score = util.ascii_score(xord)
    #         key_scores.append((key, score, xord[:20]))
    #     # key_scores = sorted(key_scores, key=lambda x: x[1], reverse=True)
    #     key_scores.sort(key=lambda x: x[1], reverse=True)
    #     print('size:%s: %s \n' % (key_size, key_scores[:10]))


    # for bc in range(2, 10):
    #     print(bc, ': ', get_distances(b64_bytes, bc)[:3])
    # # this yields that likely key sizes are 2, 5, 3, and 29

    # print('-'*30)

    keysize_guesses = [2, 5, 3, 29]

    for keysize in keysize_guesses:
        print('keysize: %s' % keysize)
        blocks = util.chunks(b64_bytes, keysize)
        transposed_blocks = util.transpose(blocks)
        keyguess = ''
        for block, block_counter in zip(transposed_blocks, itertools.count(1)):
            max_score = 0
            best_guess = ''
            print('  block %s' % block_counter)
            for key_char_guess in string.printable:
                xors = util.fixed_xor(filter(lambda x: x is not None, block), itertools.cycle(bytes(key_char_guess, 'ascii')))
                block_str = ''.join(chr(x) for x in xors)
                score = util.ascii_score(block_str)
                if score >= max_score:
                    print('  key char:', key_char_guess, 'score:', score, 'str[:30]:', block_str[:30])
                    max_score = score
                    best_guess = key_char_guess
            keyguess += best_guess
            print(keyguess)
        print('key guess: %s' % keyguess)
        print('-'*10)
    # this yields the key guesses below

    print('\n\n')

    for keyguess in ['%"', 'i~v`s', 'o~d', 'N_rh][UxZ|0C< Cbhou>ntQ1mZihd', 'Terminator X: Bring the noise']:
        xord = util.fixed_xor(b64_bytes, itertools.cycle(bytes(keyguess, 'ascii'))).decode()
        print(xord)
        print('key: %s' % keyguess)
        print('\n\n')
