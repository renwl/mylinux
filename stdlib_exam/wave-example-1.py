import wave

w = wave.open("samples/sample.wav", "r")

if w.getnchannels() == 1:
    print("mono,", end=' ')
else:
    print("stereo,", end=' ')

print(w.getsampwidth()*8, "bits,", end=' ')
print(w.getframerate(), "Hz sampling rate")

## mono, 16 bits, 44100 Hz sampling rate
