import unittest

def factorial_one(n):
    pass

def factorial_two(n):
    pass

class FactorialTestCase(unittest.TestCase):

    def test_factorial_one(self):
        self.assertEquals(1, factorial_one(1))
        self.assertEquals(1, factorial_two(1))

if __name__ == '__main__':
    unittest.main()
