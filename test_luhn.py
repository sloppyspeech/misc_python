import unittest
import luhns_number as ln

class TestLuhn(unittest.TestCase):
    
    def test_luhn(self):
        with self.assertRaises(TypeError): ln.LuhnsNumber('Raise Type Error')
        with self.assertRaises(TypeError): ln.LuhnsNumber(None)
        luhns_num=ln.LuhnsNumber(53461861341123)
        self.assertEqual(luhns_num.get_check_digit(),4)
        luhns_num=ln.LuhnsNumber(534618613411234)
        self.assertTrue(luhns_num.is_valid())
        luhns_num=ln.LuhnsNumber(35693803564380)
        self.assertEqual(luhns_num.get_check_digit(),9)
        luhns_num=ln.LuhnsNumber(356938035643809)
        self.assertTrue(luhns_num.is_valid())
        luhns_num=ln.LuhnsNumber(35693803564380)
        self.assertFalse(luhns_num.get_check_digit()==7)
        #
        luhns_num=ln.LuhnsNumber(356938035643807)
        self.assertFalse(luhns_num.is_valid())
        #


if __name__ == '__main__':
    unittest.main()
