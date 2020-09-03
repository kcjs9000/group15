import unittest
import DA_15 as proj


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual([proj.top.index[0], proj.top.index[1], proj.top.index[2]], [' Indonesia ', ' Japan ', ' China '])

    def test_somethings(self):
        self.assertTrue([proj.top.index[0], proj.top.index[1], proj.top.index[2]], [' Indonesia ', ' Japan ', ' China '])


if __name__ == '__main__':
    unittest.main()