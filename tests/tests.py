import unittest
from uselessmod.uselessmod import UselessClass

class TestUM(unittest.TestCase):
    def setUp(self):
        pass

    def test_value(self):
        f = UselessClass()
        self.assertEqual(f.value, 'blerg')

    def test_method(self):
        f = UselessClass()
        self.assertEqual(f.beep(), 'beep')

    def test_value2(self):
        f = UselessClass()
        f.value = 'notblerg'
        self.assertEqual(f.value, 'notblerg')

    def test_method2(self):
        f = UselessClass()
        f.value = True
        self.assertEqual(f.beep(), 'nobeep4u')


if __name__ == "__main__":
    unittest.main()


