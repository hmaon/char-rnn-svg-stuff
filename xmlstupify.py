#!/usr/bin/env python

import sys
import re

exp = re.compile(r'</[^>]*>')
s = sys.stdin.read()
sys.stdout.write(re.sub(exp, '</>', s))
