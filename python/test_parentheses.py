import unittest

def has_balanced_parentheses_one(string):
    pass

def has_balanced_parentheses_two(string):
    pass

class ParenthesesTestCase(unittest.TestCase):

    def test_is_empty_string_valid(self):
        self.assertTrue(has_balanced_parentheses_one(''))
        self.assertTrue(has_balanced_parentheses_two(''))

    def test_single_set_braces(self):
        self.assertTrue(has_balanced_parentheses_one('()'))
        self.assertTrue(has_balanced_parentheses_two('()'))

    def test_invalid_set_braces(self):
        self.assertFalse(has_balanced_parentheses_one('('))
        self.assertFalse(has_balanced_parentheses_two('('))

    def test_square_braces(self):
        self.assertTrue(has_balanced_parentheses_one('[]')
        self.assertTrue(has_balanced_parentheses_two('[]')

    def test_mixed_braces(self):
        self.assertTrue(has_balanced_parentheses_one('(){}[]')
        self.assertTrue(has_balanced_parentheses_two('(){}[]')

    def test_nested_braces(self):
        self.assertTrue(has_balanced_parentheses_one('({[]})')
        self.assertTrue(has_balanced_parentheses_two('({[]})')

    def test_some_lisp(self):
        self.assertTrue(has_balanced_parentheses_one('(sin (* 2 pi 1/4))')
        self.assertTrue(has_balanced_parentheses_two('(sin (* 2 pi 1/4))')

    def test_bad_mixed(self):
        self.assertFalse(has_balanced_parentheses_one('{(])[}')
        self.assertFalse(has_balanced_parentheses_two('{(])[}')

if __name__ == '__main__':
    unittest.main()
