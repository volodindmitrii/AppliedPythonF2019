import sys

from encoding_check import encode_check
from reading import reading_data


if __name__ == '__main__':
    # filename = sys.argv[1]
    pass
filename = "files/posts-utf8.json"

enc = encode_check(filename)
if enc != "fileValidationError":
    reading_data(filename, enc)


else:
    print('Формат не валиден')

    # stdout

