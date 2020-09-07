import lzma
import os


def _(*args):
    print('[Tool] ', end='')
    for arg in args:
        print(arg, end=' ')
    print()

def get_data_d(filepath):
    _("Loading file...")
    with open(filepath, 'rb') as file:
        data = file.read()
        decompress(data, filepath)
        file.close()


def check_signature(data):
    signature_list = {
        b'\x53\x43': 'SC',
        b'\x5d\x00\x00': 'LZMA',
        b'\x53\x43\x4c\x5a': 'SCLZ',
        b'\x53\x49\x47': 'SIG'
    }

    if data.startswith(b'\x53\x43'):
        return 'SC'
    elif data.startswith(b'\x5d\x00\x00'):
        return 'LZMA'
    elif data.startswith(b'\x53\x43\x4c\x5a'):
        return 'SCLZ'
    elif data.startswith(b'\x53\x49\x47'):
        return 'SIG'
    else:
        return None


def decompress(data, filepath):
    signature = check_signature(data)
    tempdata = b''

    if signature == 'SC':
        tempdata = data[26:35] + b'\x00' *4 + data[35:]


    elif signature == 'LZMA':
        tempdata = data[0:5] + b'\xff' * 8 + data[9:]


    elif signature == None:
        tempdata = data

    else:
        print("Signature not supported!")

    _(f"Detected {signature} signature")
    _(f"Decompressing {filepath}...")

    decompressor = lzma.LZMADecompressor()
    try:
        decompressed_data = decompressor.decompress(tempdata)
    except lzma.LZMAError:
        _("Input format not supported by decoder")
        return
    path, name = os.path.split(filepath.replace('.compressed', ''))
    decompressed_path = f'{path}/{os.path.splitext(name)[0]}.decompressed{os.path.splitext(name)[1]}'
    with open(decompressed_path, 'wb') as output:
        output.write(decompressed_data)
        output.close()
        _(f"Saved as {decompressed_path}")
        _("Done!\n")

