import pytest

from Jp02_ComplexNumber import *


class Test():

    def setup_method(self):
        print("\nEnvironment for test preparation")

    def test_init(self):
        with pytest.raises(Exception):
            complex_number = ComplexNumber("Hi", 2)
        with pytest.raises(Exception):
            complex_number = ComplexNumber(5, "Hello")
        with pytest.raises(Exception):
            complex_number = ComplexNumber("Hello", "World")
        with pytest.raises(Exception):
            complex_number = ComplexNumber(4, None)
        with pytest.raises(Exception):
            complex_number = ComplexNumber(None, 3)
        with pytest.raises(Exception):
            complex_number = ComplexNumber(None, None)
        complex_number = ComplexNumber(2, 3)
        assert complex_number.re == 2
        assert complex_number.img == 3
