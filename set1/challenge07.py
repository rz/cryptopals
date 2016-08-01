from Crypto.Cipher import AES

import util


if __name__ == '__main__':
    with open('data/challenge07.txt') as f:
        b64_data = f.read()
    data = util.base64_to_bytes(b64_data)
    key = 'YELLOW SUBMARINE'
    cipher = AES.new(key, AES.MODE_ECB)
    print(util.bytes_to_str(cipher.decrypt(data)))


