#!/usr/bin/env python
# -*- coding: utf-8 -*-

from optparse import OptionParser

parser = OptionParser()
parser.add_option("-f", "--from", type="str",
                  help="filename", dest="fromfile")
parser.add_option("-t", "--to", type="str",
                  help="filename", dest="tofile")

def main():
    options, args = parser.parse_args()
    f = open(options.fromfile, "r", encoding='utf-8')
    g = open(options.tofile, "r", encoding='utf-8')
    haystack = g.read()
    print(haystack)
    g.close()
    for line in f:
        if not line.strip() in haystack:
            print(line)
    f.close()

if __name__ == '__main__':
    main()
