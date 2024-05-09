class Matrix:
    @staticmethod
    def TamGiacTren(matrix):
        n = len(matrix)
        for i in range(1, n):
            for j in range(i):
                if matrix[i][j] != 0:
                    return False
        return True
