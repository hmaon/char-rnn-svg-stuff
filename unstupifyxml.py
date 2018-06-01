#!/usr/bin/env python

import sys
import re


exp = re.compile(r'<([^/ >]*)[^>]*>[^<]*')
stack = []

def unstupifyxml(s, callback = sys.stdout.write):
    for res in exp.finditer(s):
        tag = res.group()
        if tag.startswith('</>') and len(stack) > 0:
            tag = tag.replace('</>', stack.pop())
        elif tag.count('/>') == 0 or tag.startswith("<svg"):
            stack.append('</' + res.group(1) + '>')
        callback(tag)

    
if __name__ == '__main__':
    input = sys.stdin.read()
    unstupifyxml(input)
    