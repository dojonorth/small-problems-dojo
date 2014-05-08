import unittest

def factorial(n):
    pass

class FactorialTestCase(unittest.TestCase):

    def test_factorial_one(self):
        self.assertEquals(1, factorial(1))

if __name__ == '__main__':
    unittest.main()
