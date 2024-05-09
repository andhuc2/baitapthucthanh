class Matrix:
    @staticmethod
    def TrungHang(matrix):
        n = len(matrix)
        for i in range(n):
            for j in range(i + 1, n):
                if matrix[i] == matrix[j]:
                    return True
        return False
