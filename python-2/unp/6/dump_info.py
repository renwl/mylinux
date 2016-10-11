#!/usr/bin env python

import sys,urllib.request,urllib.error,urllib.parse

req=urllib.request.Request(sys.argv[1])
fd=urllib.request.urlopen(req)

print("Retrieved",fd.geturl())
info=fd.info()

for key,value in list(info.items()):
  print("%s = %s " % ( key,value))
