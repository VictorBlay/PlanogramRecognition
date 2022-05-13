import unittest
from prepare_data import prepare_data

class TestStringMethods(unittest.TestCase):

    def test_prepare_data(self):
        x = prepare_data("./queryimage")
        print(x)
        #self.assertEqual('foo'.upper(), 'FOO')

if __name__ == '__main__':
    unittest.main()