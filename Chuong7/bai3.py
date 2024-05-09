def ChuTrinh(dt):
    visited = set()

    def DFS(node, parent):
        visited.add(node)
        for neighbor in dt[node]:
            if neighbor not in visited:
                if DFS(neighbor, node):
                    return True
            elif neighbor != parent:
                return True
        return False

    for node in dt:
        if node not in visited:
            if DFS(node, None):
                return True
    return False

# Sử dụng: dt là một từ điển biểu diễn đồ thị, ví dụ: {1: [2, 3], 2: [1, 3], 3: [1, 2]}
dt = {1: [2, 3], 2: [1, 3], 3: [1, 2]}
result = ChuTrinh(dt)
print(result)  # Kết quả: True hoặc False
