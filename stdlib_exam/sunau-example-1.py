import sunau

w = sunau.open("samples/sample.au", "r")

if w.getnchannels() == 1:
    print("mono,", end=' ')
else:
    print("stereo,", end=' ')

print(w.getsampwidth()*8, "bits,", end=' ')
print(w.getframerate(), "Hz sampling rate")

## mono, 16 bits, 8012 Hz sampling rate
