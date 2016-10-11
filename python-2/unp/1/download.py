#!/usr/bin/env python

import urllib.request, urllib.parse, urllib.error,sys

f=urllib.request.urlopen(sys.argv[1])

while True:
  buf = f.read(2048)
  if not len(buf):
    break
  sys.stdout.write(buf)
