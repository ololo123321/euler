import os
import re


if __name__ == '__main__':
    files = [x for x in os.listdir('.') if re.match('p\d+\.py', x)]
    for f in sorted(files):
        print(f)
        os.system('python {}'.format(f))
