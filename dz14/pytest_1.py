import pytest
from classify_triangle import classify_triangle


def test_equilateral_triangle():
    result = classify_triangle(5, 5, 5)
    assert result == "Треугольник равносторонний"

def test_isosceles_triangle():
    result = classify_triangle(5, 5, 6)
    assert result == "Треугольник равнобедренный"

def test_scalene_triangle():
    result = classify_triangle(3, 4, 5)
    assert result == "Треугольник разносторонний"

def test_nonexistent_triangle():
    result = classify_triangle(1, 2, 4)
    assert result == "Треугольник не существует"

pytest.main()
