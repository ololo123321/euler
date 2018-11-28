import os
import re

files = [x for x in os.listdir() if re.match('p\d+\.py', x)]
for f in sorted(files):
    print(f)
    os.system('python {}'.format(f))
