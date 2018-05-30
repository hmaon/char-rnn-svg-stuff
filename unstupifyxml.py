#!/usr/bin/env python

import sys
import re


exp = re.compile(r'<([^/ >]*)[^>]*>')
s = sys.stdin.read()
stack = []

while len(s) > 0:
    res = exp.search(s)
    if res == None:
        sys.stdout.write(s)
        break
    sys.stdout.write(s[:res.start()])
    tag = res.group()
    if tag == '</>' and len(stack) > 0:
        tag = stack.pop()
    elif tag.count('/>') == 0 or tag.find("<svg") == 0:
        stack.append('</' + res.group(1) + '>')
    sys.stdout.write(tag)
    s = s[res.end():]
