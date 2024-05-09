class Matrix:
    @staticmethod
    def NhomHang(matrix):
        n = len(matrix)
        visited = set()
        for i in range(n):
            if i not in visited:
                group = [i]
                for j in range(i + 1, n):
                    if matrix[i] == matrix[j]:
                        group.append(j)
                        visited.add(j)
                if len(group) > 1:
                    print("Nhóm chỉ mục hàng giống nhau:", group)
