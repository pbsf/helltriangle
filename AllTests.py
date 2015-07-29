import unittest
from helltriangle import HellTriangle

class HellTriangleTestCase(unittest.TestCase):

    def test_example(self):
        triangle = [[6],[3,5],[9,7,1],[4,6,8,4]]
        result = HellTriangle.calculate_longest_path(triangle)
        assert result == 26

    def test_larger(self):
        triangle = [[6],[3,5],[9,7,1],[4,6,8,4],[4,3,2,1,5],[1000,2,3,4,5,6]]
        result = HellTriangle.calculate_longest_path(triangle)
        assert result == 1026

    def test_negative(self):
        triangle = [[6],[3,5],[9,7,1],[4,6,-8,4]]
        result = HellTriangle.calculate_longest_path(triangle)
        assert result == 24

    def test_single_element(self):
        triangle = [[6]]
        result = HellTriangle.calculate_longest_path(triangle)
        assert result == 6

    def test_invalid1(self):
        triangle = [[6],[3,5],[9]]
        try:
            result = HellTriangle.calculate_longest_path(triangle)
        except ValueError:
            pass
        else:
            fail("Expected ValueError")

    def test_invalid2(self):
        triangle = None
        try:
            result = HellTriangle.calculate_longest_path(triangle)
        except ValueError:
            pass
        else:
            fail("Expected ValueError")

    def test_invalid3(self):
        triangle = [[6],[3]]
        try:
            result = HellTriangle.calculate_longest_path(triangle)
        except ValueError:
            pass
        else:
            fail("Expected ValueError")

    def test_invalid4(self):
        triangle = [[6, 7]]
        try:
            result = HellTriangle.calculate_longest_path(triangle)
        except ValueError:
            pass
        else:
            fail("Expected ValueError")


    def test_invalid5(self):
        triangle = []
        try:
            result = HellTriangle.calculate_longest_path(triangle)
        except ValueError:
            pass
        else:
            fail("Expected ValueError")

    def test_invalid6(self):
        triangle = [[]]
        try:
            result = HellTriangle.calculate_longest_path(triangle)
        except ValueError:
            pass
        else:
            fail("Expected ValueError")

    def test_invalid7(self):
        triangle = [1]
        try:
            result = HellTriangle.calculate_longest_path(triangle)
        except ValueError:
            pass
        else:
            fail("Expected ValueError")



if __name__ == "__main__":
    unittest.main()
