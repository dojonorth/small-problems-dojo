import unittest

def is_palindrome_one(string):
    pass

def is_palindrome_two(string):
    pass

class PalindromeTestCase(unittest.TestCase):

    def test_is_bob_palindrome(self):
        self.assertTrue(is_palindrome_one('bob'))
        self.assertTrue(is_palindrome_two('bob'))

    def test_is_bobo_palindrome(self):
        self.assertFalse(is_palindrome_one('bobo'))
        self.assertFalse(is_palindrome_two('bobo'))

    def test_ignores_case(self):
        self.assertTrue(is_palindrome_one('Bob'))
        self.assertTrue(is_palindrome_two('Bob'))

    def test_ignores_punctuation(self):
        self.assertTrue(is_palindrome_one('A man, a plan, a canal: Panama'))
        self.assertTrue(is_palindrome_two('A man, a plan, a canal: Panama'))

if __name__ == '__main__':
    unittest.main()
