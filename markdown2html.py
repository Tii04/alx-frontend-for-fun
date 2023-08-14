#!/usr/bin/python3

import sys
import os

if ((len(sys.argv)) < 2):
    sys.stderr.write('Usage: ./markdown2html.py README.md README.html')
    exit(1)

else:
    filename = sys.argv[1]
    if not os.path.exists(filename):
        print(f'Missing {filename}')
        exit(1)

    else:
        exit(0)
