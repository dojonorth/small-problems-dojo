import unittest

def has_balanced_parentheses(string):
    pass

class ParenthesesTestCase(unittest.TestCase):

    def test_is_empty_string_valid(self):
        self.assertTrue(has_balanced_parentheses(''))

if __name__ == '__main__':
    unittest.main()
