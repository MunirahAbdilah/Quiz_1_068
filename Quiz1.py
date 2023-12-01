# Nama : Munirah Abdilah
# Nim: F55122068
# Kelas: B

class MatrixOperations:
    def __init__(self, matrix):
        self.matrix = matrix

    def find_min_max(self):
        flat_matrix = [element for row in self.matrix for element in row]
        return min(flat_matrix), max(flat_matrix)

    def transpose_matrix(self):
        return [[self.matrix[j][i] for j in range(len(self.matrix))] for i in range(len(self.matrix[0]))]

    def multiply_matrices(self, other_matrix):
        result = [[0 for _ in range(len(other_matrix[0]))] for _ in range(len(self.matrix))]
        for i in range(len(self.matrix)):
            for j in range(len(other_matrix[0])):
                for k in range(len(other_matrix)):
                    result[i][j] += self.matrix[i][k] * other_matrix[k][j]
        return result

    def add_matrices(self, other_matrix):
        return [[self.matrix[i][j] + other_matrix[i][j] for j in range(len(self.matrix[0]))] for i in range(len(self.matrix))]


if __name__ == "__main__":
    matrix_A = [
        [34, 100, 12],
        [72, 24, 55],
        [61, 20, 19]
    ]

    operations_A = MatrixOperations(matrix_A)
    
    # 1. Menghitung element terbesar dan terkecil
    min_value, max_value = operations_A.find_min_max()
    print(f"Elemen Terkecil: {min_value}")
    print(f"Elemen Terbesar: {max_value}")

    # 2. Transpose matrix 
    transposed_A = operations_A.transpose_matrix()
    print("\nMatrix Transpose:")
    for row in transposed_A:
        print(row)

    # 3. Menghitung perkalian matrix A dan transpose matriks A
    matrix_B = operations_A.transpose_matrix()
    multiplication_result = operations_A.multiply_matrices(matrix_B)
    print("\nHasil perkalian matriks A dan transpose matriks A:")
    for row in multiplication_result:
        print(row)

    # 4. Menghitung penjumlahan matrix A dan transpose matriks A
    addition_result = operations_A.add_matrices(transposed_A)
    print("\nHasil Penjumlahan matriks A dan transpose matriks A:")
    for row in addition_result:
        print(row)
