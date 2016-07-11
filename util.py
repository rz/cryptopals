import base64
import itertools
import string


def str_to_bytes(input_str, encoding='utf8'):
    return bytes(input_str, encoding)


def hex_to_bytes(input_str):
    return bytes.fromhex(input_str)


def bytes_to_hex(bs):
    import binascii
    return binascii.hexlify(bs).decode('utf8')


def base64_to_bytes(input_str):
    return base64.b64decode(input_str)


def fixed_xor(a, b):
    xors = [i ^ j for i, j in zip(a, b)]
    return bytes(xors)


def ascii_score(s):
    "returns the number of characters in the given string that are ascii digits, letters or space"
    alphabet = string.digits + string.ascii_letters + ' '
    return len([c for c in s if c in alphabet])


def hamming_distance(a, b):
    """compute the hamming distance between two byte sequences of the same length"""
    if len(a) != len(b):
        raise ValueError('Undefined for unequal lengths: %s, %s' % (len(a), len(b)))
    xors = [i ^ j for i, j in zip(a, b)]
    return ''.join(bin(x) for x in xors).count('1')


def binary_peak(bs):
    """returns a string of 0s and 1s ie the binary representation of the given byte sequence"""
    return ''.join(bin(b)[2:].rjust(8, '0') for b in bs)


def chunks(iterable, size):
    return [iterable[i:i+size] for i in range(0, len(iterable), size)]


def transpose(iterable):
    return list(map(list, itertools.zip_longest(*iterable)))

