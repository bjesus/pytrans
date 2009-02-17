#!/usr/bin/env python
# -*- coding: utf-8 -
# Pytrans is a frontend to babylon
# Version 1.1

from urllib2 import urlopen
from urllib import urlencode
from sys import argv

base_url = "http://translation.babylon.com/post_post.php"

def strip(s):
    intag = [False]
    def chk(c):
        if intag[0]:
            intag[0] = (c != '>')
            return False
        elif c == '<':
            intag[0] = True
            return False
        return True
    return ''.join(c for c in s if chk(c))

def translate(term):
    if term[0] == '\xd7':
        params = urlencode(dict(lps=14, lpt=0, mytextarea1=term))
    elif term[0] in ['\xd9','\xd8']:
        params = urlencode(dict(lps=15, lpt=14, mytextarea1=term))
    else:
        params = urlencode(dict(lps=0, lpt=14, mytextarea1=term))
    page = urlopen(base_url, params).read()
    return strip(page).replace("\n", '').replace("&nbsp;", "\n").replace("  ", "")
    
if __name__ == "__main__":
    if len(argv) == 1:
        print "What do you want to translate?"
        exit()
    term = " ".join(argv[1:])
    output = translate(term)
    print term
    print output
