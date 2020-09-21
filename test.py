import os
import re


if __name__ == '__main__':
    problems_dir = "./problems"
    pattern = r'p\d+.*\.py'
    files = sorted(x for x in os.listdir(problems_dir) if re.match(pattern, x))
    for f in sorted(files):
        print(f)
        os.system(f'python {os.path.join(problems_dir, f)}')
        print()
