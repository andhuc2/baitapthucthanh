def BacDinh(dt, v):
    return len(dt[v])

# Sử dụng: dt là một từ điển biểu diễn đồ thị, v là một đỉnh
dt = {1: [2, 3], 2: [1, 3], 3: [1, 2]}
vertex = 1
result = BacDinh(dt, vertex)
print(result)  # Kết quả: Bậc của đỉnh v
