import unittest

def has_balanced_parentheses_one(string):
    pass

def has_balanced_parentheses_two(string):
    pass

class ParenthesesTestCase(unittest.TestCase):

    def test_is_empty_string_valid(self):
        self.assertTrue(has_balanced_parentheses_one(''))
        self.assertTrue(has_balanced_parentheses_two(''))

if __name__ == '__main__':
    unittest.main()
