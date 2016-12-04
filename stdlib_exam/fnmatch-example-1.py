#coding=utf-8
import fnmatch
import os

for file in os.listdir(r"E:\baiduyundownload\宝宝的歌"):
    if fnmatch.fnmatch(file, "*.3gp"):
        print(file)

## sample.jpg
