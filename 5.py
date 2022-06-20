class Python:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def Area(self):
        self.Area_of_rectangle=self.length*self.breadth
        print("Area of Rectangle with length ",self.length,"and Breadth ",self.breadth,"is",self.Area_of_rectangle)
    def Perimeter(self):
        self.Perimeter_of_rectangle=2*(self.length+self.breadth)
        print("Perimeter of Rectangle with length {0} and Breadth {1} is {2}".format(self.length,self.breadth,self.Perimeter_of_rectangle))
a=int(input("Enter Length of a Rectangle : "))
b=int(input("Enter Breadth of a Rectangle : "))
c1=Python(a,b)
while True:
    print("1.Area\n2.Perimeter\n3.Exit")
    var=int(input("Enter Your Choice : "))
    if var==1:
        c1.Area()
    elif var==2:
        c1.Perimeter()
    else:
        print("Exit")
        break

