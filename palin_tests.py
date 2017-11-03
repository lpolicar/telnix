import unittest
from palin import int_to_base, get_palindromic_min_base


class UnitTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    def setUp(self):
        pass

    def check_bin_hex_oct(self, n, base):
        act = ''.join(int_to_base(n, base)).upper()
        func = {2: bin, 16: hex, 8: oct}[base]
        exp = func(n)[2:].upper()
        print(n, "to base", base, "-->", "expected:", exp, "actual:", act)
        self.assertEqual(act, exp)

    # validate boundary values against result from built-in functions bin(), hex(), oct()
    def test_int_to_base(self):
        for i in [0, 1, 2, 999, 1000, 1001]:
            for base in [2, 8, 16]:
                self.check_bin_hex_oct(i, base)

    def test_get_palindromic_min_base(self):
        # validate against the given first twenty output from the exam
        exp_data = zip(range(1, 21), (2, 3, 2, 3, 2, 5, 2, 3, 2, 3, 10, 5, 3, 6, 2, 3, 2, 5, 18, 3))
        for n, exp_base in exp_data:
            act_base = get_palindromic_min_base(n)
            print(n, ",", "act:", act_base, "exp:", exp_base)
            # assert exp_base == act_base
            self.assertEqual(exp_base, act_base)

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        pass


if __name__ == "__main__":
    unittest.main()
