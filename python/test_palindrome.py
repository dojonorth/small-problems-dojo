import unittest

def is_palindrome_one(string):
    pass

def is_palindrome_two(string):
    pass

class PalindromeTestCase(unittest.TestCase):

    def test_is_bob_palindrome(self):
        self.assertTrue(is_palindrome_one('bob'))
        self.assertTrue(is_palindrome_two('bob'))

if __name__ == '__main__':
    unittest.main()
