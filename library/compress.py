import lzma
import os
from hashlib import md5

def _(*args):
    print('[Tool] ', end='')
    for arg in args:
        print(arg, end=' ')
    print()


def get_data_c(filepath, signature: str):
    _("Loading file...")
    with open(filepath, 'rb') as file:
        data = file.read()
        compress(data, filepath, signature = signature)
        file.close()


def len_2_bytes(datalen, max_len=4):
    data = []
    while datalen > 0:
        item = datalen % 256
        datalen = int(datalen / 256)
        data.append(item)
    while len(data) < max_len:
        data.append(0)
    return data


def compress(data, filepath, signature:str, max_len=4):
    supported_signatures = [
        'lzma',
        'sc'
    ]
    if signature in supported_signatures:
        _(f"Compressing {filepath}...")
        filters = [
            {
                "id": lzma.FILTER_LZMA1,
                "dict_size": 256 * 1024,
                "lc": 3,
                "lp": 0,
                "pb": 2,
                "mode": lzma.MODE_NORMAL
            },
        ]

        compressed_data = lzma.compress(data, format=lzma.FORMAT_ALONE, filters=filters)
        lzmadata = bytearray()

        for i in range(0, 5):
            lzmadata.append(compressed_data[i])
        data_size = len_2_bytes(len(data), max_len)

        for size in data_size:
            lzmadata.append(size)
        for i in range(13, len(compressed_data)):
            lzmadata.append(compressed_data[i])

        if signature.lower() == 'sc':
            header = b'SC' + b'\x00' *3 + b'\x01' + b'\x00' *3 + b'\x10'
            data_hash = md5(data)
            lzmadata = header + data_hash.digest() + lzmadata


        path, name = os.path.split(filepath.replace('.decompressed', ''))
        compressed_path = f'{path}/{os.path.splitext(name)[0]}.compressed{os.path.splitext(name)[1]}'
        with open(compressed_path, 'wb') as output:
            output.write(lzmadata)
            output.close()
            _(f"Saved as {compressed_path}")
            _("Done!\n")

    else:
        print(f"{signature} signature not supported")
        return
