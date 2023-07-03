# Создайте класс Матрица. Добавьте методы для:
# вывода на печать,
# сравнения,
# сложения,
# *умножения матриц

class Matrix:
    def __init__(self, rows, columns):
        # Инициализирует объект матрицы с заданным количеством строк и столбцов.
        self.rows = rows
        self.columns = columns
        self.data = [[0] * columns for _ in range(rows)]

    def __str__(self):
        # Возвращает строковое представление матрицы.
        matrix_str = ""
        for row in self.data:
            matrix_str += " ".join(str(element) for element in row)
            matrix_str += "\n"
        return matrix_str

    def __eq__(self, other):
        # Проверяет, равны ли две матрицы.
        if isinstance(other, Matrix):
            if self.rows != other.rows or self.columns != other.columns:
                return False
            for i in range(self.rows):
                for j in range(self.columns):
                    if self.data[i][j] != other.data[i][j]:
                        return False
            return True
        return False

    def __add__(self, other):
        # Складывает две матрицы одинаковых размеров.
        if isinstance(other, Matrix) and self.rows == other.rows and self.columns == other.columns:
            result = Matrix(self.rows, self.columns)
            for i in range(self.rows):
                for j in range(self.columns):
                    result.data[i][j] = self.data[i][j] + other.data[i][j]
            return result
        else:
            raise ValueError("Cannot add matrices of different sizes.")

    def __mul__(self, other):
        # Умножает две матрицы.
        if isinstance(other, Matrix) and self.columns == other.rows:
            result = Matrix(self.rows, other.columns)
            for i in range(self.rows):
                for j in range(other.columns):
                    for k in range(self.columns):
                        result.data[i][j] += self.data[i][k] * other.data[k][j]
            return result
        else:
            raise ValueError("Cannot multiply matrices with incompatible sizes.")

# Создание матрицы
matrix1 = Matrix(2, 2)
matrix1.data = [[4, 2], [3, 7]]

matrix2 = Matrix(2, 2)
matrix2.data = [[5, 8], [6, 9]]

# Вывод на печать
print(matrix1)
print(matrix2)

# Сравнение матриц
print(matrix1 == matrix2)

# Сложение матриц
sum_matrix = matrix1 + matrix2
print(sum_matrix)

# Умножение матриц
# matrix3 = Matrix(2, 3)
# matrix3.data = [[12, 15, 33], [14, 15, 66]]

# matrix4 = Matrix(3, 2)
# matrix4.data = [[17, 28], [19, 11], [1, 12]]

product_matrix = matrix1 * matrix2
print(product_matrix)

