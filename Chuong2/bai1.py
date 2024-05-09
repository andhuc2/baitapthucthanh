class Matrix:
    @staticmethod
    def DoiXung(matrix):
        n = len(matrix)
        for i in range(n):
            for j in range(i + 1, n):
                if matrix[i][j] != matrix[j][i]:
                    return False
        return True
