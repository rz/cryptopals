import collections

import util


if __name__ == '__main__':
    with open('data/challenge08.txt') as f:
        hex_strings = [l.replace('\n', '') for l in f.readlines()]
    for i, h in enumerate(hex_strings):
        bs = util.hex_to_bytes(h)
        chunks = util.chunks(bs, 16)
        counter = collections.Counter(chunks)
        sorted_counts = sorted(counter.items(), key=lambda x: x[1], reverse=True)
        if sorted_counts[0][1] > 1:
            print('ECB encoded on line:', i)
            print('raw hex:', h)
            print('block counts:', sorted_counts)

