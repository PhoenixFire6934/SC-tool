import argparse
import os

from library.decompress import get_data_d
from library.compress import  get_data_c

parser = argparse.ArgumentParser(description='Decompress/compress game assets')
parser.add_argument('-d', '-decompress' , type=str, nargs=1, help='decompress .sc or .csv files')
parser.add_argument('-c', '-compress' , type=str, nargs=2, help='compress .sc or .csv files')
args = parser.parse_args()

if not args.d and not args.c:
    print('Usage:\n-> decompress: python main.py -d <file_path>\n-> compress: python main.py -c <file_path> <signature> ')

if args.d:
    path = args.d[0]
    if os.path.isfile(path):
        get_data_d(path)
    elif os.path.isdir(path):
        for filename in os.listdir(path):
            get_data_d(f"{path}/{filename}")


elif args.c:
    path = args.c[1]
    signature = args.c[0]
    if os.path.isfile(path):
        get_data_c(path, signature)
    elif os.path.isdir(path):
        for filename in os.listdir(path):
            get_data_c(f"{path}/{filename}", signature)
