import unittest
from homework import Practice

class Test(unittest.TestCase):
    def test_task_1(self):
        a =[1,1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
        b =[1,2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        check = [1, 2, 3, 5, 8, 13]
        result = Practice.task_1(a, b)
        self.assertEqual(check, result)

    def test_task_2(self):
        str = "I am a good developer. I am also a writer"
        check = 5
        result = Practice.task_2(str)
        self.assertEqual(check, result)

    def test_task_3(self):
        result = Practice.task_3(3)
        self.assertTrue(result)

    def test_task_4(self):
        check = 5
        result = Practice.task_4(59)
        self.assertEqual(check, result)

    def test_task_5(self):
        check = [2, 3, 4, 6, 7, 10, 0]
        result = Practice.task_5([0,2,3,4,6,7,10])
        self.assertListEqual(check, result)

    def test_task_6(self):
        result = Practice.task_6([5, 7, 9, 11])
        self.assertTrue(result)

    def test_task_7(self):
        check = 5
        result = Practice.task_7([5, 3, 4, 3, 4])
        self.assertEqual(check, result)

    def test_task_8(self):
        check = 5
        result = Practice.task_8([1,2,3,4,6,7,8])
        self.assertEqual(check, result)

    def test_task_9(self):
        check = 3
        result = Practice.task_9([1,2,3, (1,2), 3])
        self.assertEqual(check, result)

    def test_task_10(self):
        check = "sredoC dna dlroW olleH"
        result = Practice.task_10("Hello World and Coders")
        self.assertEqual(check, result)

    def test_task_11(self):
        check = "1:3"
        result = Practice.task_11(63)
        self.assertEqual(check, result)

    def test_task_12(self):
        self.assertEqual("time", Practice.task_12("fun&!! time"))
        self.assertEqual("love", Practice.task_12("I love dogs"))

    def test_task_13(self):
        check = "Michele is name My"
        result = Practice.task_13("My name is Michele")
        self.assertEqual(check, result)

    def test_task_14(self):
        self.assertTrue(Practice.task_14())

    def test_task_15(self):
        check = [4, 16]
        result = Practice.task_15([1, 4, 9, 16])
        self.assertEqual(check, result)

    def test_task_16(self):
        check = 10
        result = Practice.task_16(4)
        self.assertEqual(check, result)

    def test_task_17(self):
        check = 24
        result = Practice.task_17(4)
        self.assertEqual(check, result)

    def test_task_18(self):
        check = "bcdE"
        result = Practice.task_18("abcd")
        self.assertEqual(check, result)

    def test_task_19(self):
        check = "abcde"
        result = Practice.task_19("edcba")
        self.assertEqual(check, result)

    def test_task_20(self):
        self.assertTrue(Practice.task_20(4,6))
        self.assertFalse(Practice.task_20(6,4))
        self.assertEqual('-1',Practice.task_20(4,4))

if __name__ == '__main__':
    unittest.main()
