def Giao(a, b):
    unique_a = set(a)
    unique_b = set(b)
    intersection = sorted(list(unique_a.intersection(unique_b)))
    return intersection

# Sử dụng
a = [1, 5, 3, 7, 9, 4, 2]
b = [9, 6, 2, 3, 8]
result = Giao(a, b)
print(result)  # Kết quả: [3, 9]
