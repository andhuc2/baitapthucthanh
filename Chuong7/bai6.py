def SoCungVao(dt, v):
    count = 0
    for node in dt:
        if v in dt[node]:
            count += 1
    return count

# Sử dụng: dt là một từ điển biểu diễn đồ thị, v là một đỉnh
dt = {1: [2, 3], 2: [1, 3], 3: [1, 2]}
vertex = 3
result = SoCungVao(dt, vertex)
print(result)  # Kết quả: Số cung đi vào đỉnh v
