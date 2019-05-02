from collections import Counter
import unittest


def is_permutation(wordA, wordB):
    counterA = Counter(wordA)
    coutnerB = Counter(wordB)
    
    for key in counterA.keys():
        if key not in coutnerB or coutnerB[key] != counterA[key]:
            return False

    return True


""" Driver code """

class Test(unittest.TestCase):
    dataT = (
        ('Hello', 'ellHo'),
        ('3563476', '7334566'),
        ('wef34f', 'wffe34')
    )
    dataF = (
        ('abcd', 'd2cba'),
        ('2354', '1234'),
        ('dcw4f', 'dcw5f'),
    )

    def test_check_permutation(self):
        #true check
        for test_strings in self.dataT:
            result = is_permutation(*test_strings)
            self.assertTrue(result)

        #false check
        for test_strings in self.dataF:
            result = is_permutation(*test_strings)
            self.assertFalse(*test_strings)


if __name__ == "__main__":
    unittest.main()
