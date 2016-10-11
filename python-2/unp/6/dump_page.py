#!/usr/bin env python

import sys,urllib.request,urllib.error,urllib.parse

req=urllib.request.Request(sys.argv[1])
fd=urllib.request.urlopen(req)

while 1:
  data=fd.read(1024)
  if not len(data):
    break

  sys.stdout.write(data)
