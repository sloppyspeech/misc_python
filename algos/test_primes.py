import unittest
import primes as prm


class TestPrimes(unittest.TestCase):
    def test_primes(self):
        prime_below200 = [
            2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61,
            67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137,
            139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199
        ]
        self.assertTrue(prm.is_prime(2))
        self.assertTrue(prm.is_prime(3))
        self.assertFalse(prm.is_prime(4))
        self.assertTrue(prm.is_prime(5))
        self.assertFalse(prm.is_prime(6))
        self.assertTrue(prm.is_prime(7))
        self.assertTrue(prm.is_prime(11))
        self.assertFalse(prm.is_prime(12))
        self.assertTrue(prm.is_prime(13))
        self.assertEqual(prm.get_primes_by_sieve(200),prime_below200)

if __name__ == '__main__':
    unittest.main()
