import subprocess

stat, output = subprocess.getstatusoutput("ls -lR")

print("status", "=>", stat)
print("output", "=>", len(output), "bytes")

## status => 0
## output => 171046 bytes
