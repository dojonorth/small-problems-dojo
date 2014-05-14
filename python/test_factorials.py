import unittest

def factorial_one(n):
    pass

def factorial_two(n):
    pass

class FactorialTestCase(unittest.TestCase):

    def test_factorial_one(self):
        self.assertEquals(1, factorial_one(1))
        self.assertEquals(1, factorial_two(1))

    def test_factorial_four(self):
        self.assertEquals(24, factorial_one(4))
        self.assertEquals(24, factorial_two(4))

    def test_factorial_ten(self):
        self.assertEquals(3628800, factorial_one(10))
        self.assertEquals(3628800, factorial_two(10))

if __name__ == '__main__':
    unittest.main()
