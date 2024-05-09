def ChuaDinh(dt, v):
    return v in dt

# Sử dụng: dt là một từ điển biểu diễn đồ thị, v là một đỉnh
dt = {1: [2, 3], 2: [1, 3], 3: [1, 2]}
vertex = 4
result = ChuaDinh(dt, vertex)
print(result)  # Kết quả: True hoặc False
