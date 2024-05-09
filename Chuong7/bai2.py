def SoThanhPhan(dt):
    visited = set()

    def DFS(node):
        visited.add(node)
        for neighbor in dt[node]:
            if neighbor not in visited:
                DFS(neighbor)

    count = 0
    for node in dt:
        if node not in visited:
            count += 1
            DFS(node)

    return count

# Sử dụng: dt là một từ điển biểu diễn đồ thị, ví dụ: {1: [2, 3], 2: [1], 3: [1]}
dt = {1: [2, 3], 2: [1], 3: [1]}
result = SoThanhPhan(dt)
print(result)  # Kết quả: Số thành phần liên thông
