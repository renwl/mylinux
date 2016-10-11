
def convert(func,seq):
    return[func (eachNum ) for eachNum in seq]

myseq=(123,45.67,-6.2e8,99999999)
print(convert(int,myseq))
print(convert(int,myseq))
print(convert(float,myseq))
