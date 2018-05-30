#!/usr/bin/env python

import sys
import re


exp = re.compile(r'<([^/ >]*)[^>]*>[^<]*')
s = sys.stdin.read()
stack = []


for res in exp.finditer(s):
    tag = res.group()
    if tag.startswith('</>') and len(stack) > 0:
        tag = tag.replace('</>', stack.pop())
    elif tag.count('/>') == 0 or tag.startswith("<svg"):
        stack.append('</' + res.group(1) + '>')
    sys.stdout.write(tag)
