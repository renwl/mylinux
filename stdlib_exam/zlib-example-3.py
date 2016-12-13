import zlib

encoder = zlib.compressobj()

data = encoder.compress(b"life")
data = data + encoder.compress(b" of ")
data = data + encoder.compress(b"brian")
data = data + encoder.flush()

print(repr(data))
print(repr(zlib.decompress(data)))

## 'x\234\313\311LKU\310OSH*\312L\314\003\000!\010\004\302'
## 'life of brian'
