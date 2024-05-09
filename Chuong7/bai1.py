def LienThong(dt):
    visited = set()

    def DFS(node):
        visited.add(node)
        for neighbor in dt[node]:
            if neighbor not in visited:
                DFS(neighbor)

    # Chọn một đỉnh bất kỳ làm đỉnh bắt đầu
    start_node = next(iter(dt))
    DFS(start_node)

    return len(visited) == len(dt)

# Sử dụng: dt là một từ điển biểu diễn đồ thị, ví dụ: {1: [2, 3], 2: [1], 3: [1]}
dt = {1: [2, 3], 2: [1], 3: [1]}
result = LienThong(dt)
print(result)  # Kết quả: True hoặc False
