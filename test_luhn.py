import unittest
import luhns_number as ln

class TestLuhn(unittest.TestCase):
    
    def test_luhn(self):
        self.assertEqual(ln.get_check_digit(53461861341123),4)
        self.assertTrue(ln.get_check_digit(35693803564380)==9)
        

if __name__ == '__main__':
    unittest.main()