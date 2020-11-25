class Complex:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    # Overloaded print statement
    def __str__(self):
        return "%s + %si" % (self.real, self.imaginary)

    # Overloaded add
    def __add__(self, right):
        return Complex(self.real + right.real, self. imaginary + right.imaginary)

    # Overloaded subtract
    def __sub__(self, right):
        return Complex(self.real - right.real, self. imaginary - right.imaginary)

    # Overloaded multiplication
    def __mul__(self, right):
        mult_real = self.real * right.real - self.imaginary * right.imaginary
        mult_imaginary = self.real * right.imaginary + self.imaginary * right.real
        return Complex(mult_real, mult_imaginary)

    # Overloaded division (using the / operator)
    def __truediv__(self, right):
        top = self.__mul__(Complex(right.real, -right.imaginary))
        bottom = (right.real ** 2) - (right.imaginary * -right.imaginary)
        return Complex(top.real / bottom, top.imaginary / bottom)

# code starts here
if __name__ == "__main__":
    first = input('enter first num: ').split()
    first = [int(x) for x in first]

    second = input('enter second num: ').split()
    second = [int(x) for x in second]

    # Note: The * means that we are passing in the variable as a list argument.
    # Think of passing in an *args argument as opposed to receiving an *args parameter.
    num1 = Complex(*first)
    num2 = Complex(*second)

    print(num1 + num2, num1 - num2, num1 * num2, num1 / num2, sep='\n')
