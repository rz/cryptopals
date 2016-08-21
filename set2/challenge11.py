import collections
import random

import util


def encrypt_aes_random(plainbytes):
    key = util.get_random_bytes(16)

    prepad = util.get_random_bytes(random.randint(5, 10))
    postpad = util.get_random_bytes(random.randint(5, 10))
    padded_plainbytes = prepad + plainbytes + postpad

    # need to make sure that plaintext ends up being a multiple of 16 bytes
    aes_pad_length = 16 - len(padded_plainbytes) % 16
    padded_plainbytes += bytes(0 for _ in range(aes_pad_length))

    mode = random.choice(['ecb', 'cbc'])
    iv = util.get_random_bytes(16)  # encrypt_aesignores the iv in ecb mode
    print('encrypting using mode:', mode)

    return util.encrypt_aes(padded_plainbytes, key, mode, iv)


def ecb_cbc_oracle():
    plainbytes = b'\x00'*64
    cipherbytes = encrypt_aes_random(plainbytes)

    # look at the middle of our cipher text and look for a repeating sequence of 16 bytes
    middlebytes = cipherbytes[16:48]
    chunks = util.chunks(middlebytes, 16)
    counter = collections.Counter(chunks)
    sorted_counts = sorted(counter.items(), key=lambda x: x[1], reverse=True)
    if sorted_counts[0][1] > 1:
        mode = 'ecb'
    else:
        mode = 'cbc'
    return mode


if __name__ == '__main__':
    for _ in range(50):
        detected_mode = ecb_cbc_oracle()
        print('detected mode:', detected_mode, end='\n\n')
