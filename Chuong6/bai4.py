def Hop(a, b):
    unique_a = set(a)
    unique_b = set(b)
    union = sorted(list(unique_a.union(unique_b)))
    return union

# Sử dụng
a = [1, 5, 3, 7, 9, 4, 2]
b = [9, 6, 2, 3, 8]
result = Hop(a, b)
print(result)  # Kết quả: [1, 2, 3, 4, 5, 6, 7, 8, 9]
