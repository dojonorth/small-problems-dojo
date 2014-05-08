import unittest

def is_palindrome(string):
    pass

class PalindromeTestCase(unittest.TestCase):

    def test_is_bob_palindrome(self):
        self.assertTrue(is_palindrome('bob'))

if __name__ == '__main__':
    unittest.main()
