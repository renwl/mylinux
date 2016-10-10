class NextClass:
    def printer(self,text):
        self.message=text
        print(self.message)
x=NextClass()
x.printer("instance call")
x.message
NextClass.printer(x,"hello")
