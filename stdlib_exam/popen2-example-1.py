import popen2, string

fin, fout = popen2.popen2("sort")

fout.write("foo\n")
fout.write("bar\n")
fout.close()

print(fin.readline(), end=' ')
print(fin.readline(), end=' ')
fin.close()

## bar
## foo
