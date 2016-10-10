class Indexer:
    data=[1,2,3,4,5,6,7,8,9]
    def __getitem__(self,index):
        print("getitem:",index)
        return self.data[index]

x=Indexer()
print(x[0])
print(x[1])
print(x[-1])
print(x[1:3])
print(x[::2])

for i in x:
    print(i,end="**")
