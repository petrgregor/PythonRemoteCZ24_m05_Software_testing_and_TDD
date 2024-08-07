class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __eq__(self, other):
        return self.real == other.real and self.imag == other.imag

    def __lt__(self, other):
        return self.absolute_value() < other.absolute_value()

    def __gt__(self, other):
        return self.absolute_value() > other.absolute_value()

    def __repr__(self):
        return f'ComplexNumber({self.real}, {self.imag})'

    def __str__(self):
        return f'{self.real} + {self.imag}i'

    @property
    def real(self):
        return self._real

    @real.setter
    def real(self, value):
        self._real = value

    @property
    def imag(self):
        return self._imag

    @imag.setter
    def imag(self, value):
        self._imag = value

    def add(self, other):
        return ComplexNumber(self.real + other.real, self.imag + other.imag)

    def subtract(self, other):
        return ComplexNumber(self.real - other.real, self.imag - other.imag)

    def multiply(self, other):
        real = self.real * other.real - self.imag * other.imag
        imag = self.real * other.imag + self.imag * other.real
        return ComplexNumber(real, imag)

    def divide(self, other):
        denom = other.real**2 + other.imag**2
        real = (self.real * other.real + self.imag * other.imag) / denom
        imag = (self.imag * other.real - self.real * other.imag) / denom
        return ComplexNumber(real, imag)

    def conjugate(self):
        return ComplexNumber(self.real, -self.imag)

    def absolute_value(self):
        return (self.real**2 + self.imag**2) ** 0.5
