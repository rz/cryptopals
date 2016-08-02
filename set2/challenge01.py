import util


def pkcs7_pad(text_str, block_size):
    text_bytes = util.str_to_bytes(text_str)
    padding_length = block_size - len(text_bytes) % block_size
    text_bytes += bytes(padding_length for _ in range(padding_length))
    return text_bytes


if __name__ == '__main__':
    print(pkcs7_pad('YELLOW SUBMARINE', 20))

