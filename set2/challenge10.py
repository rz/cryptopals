from Crypto.Cipher import AES

import util


def decrypt_aes_ecb(ciphertext, key):
    cipher = AES.new(key, AES.MODE_ECB)
    return cipher.decrypt(ciphertext)


def encrypt_aes_ecb(plaintext, key):
    cipher = AES.new(key, AES.MODE_ECB)
    return cipher.encrypt(plaintext)


def encrypt_aes_cbc(plainbytes, key, iv):
    block_size = len(iv)
    blocks = util.chunks(plainbytes, block_size)
    x = iv
    ciphertext = bytes()
    for block in blocks:
        encrypted_block = encrypt_aes_ecb(util.fixed_xor(block, x), key)
        ciphertext += encrypted_block
        x = encrypted_block
    return ciphertext


def decrypt_aes_cbc(cipherbytes, key, iv):
    block_size = len(iv)
    blocks = util.chunks(cipherbytes, block_size)
    x = iv
    plaintext = bytes()
    for block in blocks:
        decrypted_block = decrypt_aes_ecb(block, key)
        plaintext += util.fixed_xor(x, decrypted_block)
        x = block
    return plaintext


if __name__ == '__main__':
    with open('data/challenge10.txt') as f:
        cipherbytes = util.base64_to_bytes(f.read())
    plainbytes = decrypt_aes_cbc(cipherbytes, key='YELLOW SUBMARINE', iv=b'\x00'*16)
    print(util.bytes_to_str(plainbytes))

