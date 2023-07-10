import unittest
from classify_triangle import classify_triangle


class TriangleClassificationTestCase(unittest.TestCase):
    def test_equilateral_triangle(self):
        result = classify_triangle(5, 5, 5)
        self.assertEqual(result, "Треугольник равносторонний")

    def test_isosceles_triangle(self):
        result = classify_triangle(5, 5, 6)
        self.assertEqual(result, "Треугольник равнобедренный")

    def test_scalene_triangle(self):
        result = classify_triangle(3, 4, 5)
        self.assertEqual(result, "Треугольник разносторонний")

    def test_nonexistent_triangle(self):
        result = classify_triangle(1, 2, 4)
        self.assertEqual(result, "Треугольник не существует")

unittest.main()
