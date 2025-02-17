import unittest
import calc


class TestCalc(unittest.TestCase):              # we can give any name to the class

    def test_add(self):                     # we have to start the method name like 'test'
        # result = calc.add(5,15)   
        self.assertEqual(calc.add(5,15), 20)
        self.assertEqual(calc.add(2,21), 23)
        self.assertEqual(calc.add(-9, 9), 0)
        self.assertEqual(calc.add(-1, -1), -2)

    def test_subtract(self):
        self.assertEqual(calc.diff(10,5),5)
        self.assertEqual(calc.diff(-5,5),-10)
        self.assertEqual(calc.diff(-2,-5),3)

    def test_multiply(self):
        self.assertEqual(calc.mul(2,2),4)
        self.assertEqual(calc.mul(-5,2),-10)
        self.assertEqual(calc.mul(-10,-5),50)

    def test_division(self):
        self.assertEqual(calc.div(10,2),5)
        self.assertEqual(calc.div(-20,5),-4)
        self.assertEqual(calc.div(-2,-2),1)

        self.assertRaises(ZeroDivisionError, calc.div, 10, 0)

        with self.assertRaises(ZeroDivisionError):          # another way of the above code
            calc.div(21,0)






# to run python3 -m unittest test_calc.py, to remove this behaviour

if __name__ == '__main__':
    unittest.main()