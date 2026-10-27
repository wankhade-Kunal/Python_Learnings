# print(1 + 2) #3 (adding)
# print("kunal" + "wankhade") #concatenate
# print([1,2,3] + [4,5,6]) # merge


class Complex:
    def __init__(self, real, img):
        self.real = real
        self.imaginary = img

    def showNumber(self):
        print(self.real,"i +", self.imaginary,"j")

    # __add__ is dunder function denote with (__ __)
    def __add__(self, num2): 
        newReal = self.real + num2.real
        newImg = self.imaginary + num2.imaginary
        return Complex(newReal, newImg)

num1 = Complex(1,7)
num1.showNumber()

num2 =  Complex(2,3)
num2.showNumber()

num3 = num1 + num2
num3.showNumber()