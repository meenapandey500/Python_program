class aaa:
    def _init__(self):
        self.__a=0
    def increment(self):
        self.__a=self.__a+1
    def decrement(self):
        self.__a=self.__a-1
    def display(self):
        print("a=",self.__a)
#main program
a1=aaa()
a1.increment( )
a1.display()
a1.increment()
a1.display()
a1.decrement()
a1.display()
