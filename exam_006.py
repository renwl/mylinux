class Squares:
    def __init__(self,start,stop):
        self.value = start -1
        self.stop = stop
        print("****init****")
    def __iter__(self):
        print("****iter****")
        return self
    def __next__(self):
        print("****next****")
        if self.value==self.stop:
            raise StopIteration
        self.value+=1
        return self.value**2

for i in Squares(1,5):
    print("i= ",i)
