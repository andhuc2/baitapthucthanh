def SoCungRa(dt, v):
    return len(dt[v])

# Sử dụng: dt là một từ điển biểu diễn đồ thị, v là một đỉnh
dt = {1: [2, 3], 2: [1, 3], 3: [1, 2]}
vertex = 3
result = SoCungRa(dt, vertex)
print(result)  # Kết quả: Số cung đi ra khỏi đỉnh v
