def Hieu(a, b):
    unique_a = set(a)
    unique_b = set(b)
    difference = sorted(list(unique_a.difference(unique_b)))
    return difference

# Sử dụng
a = [1, 5, 3, 7, 9, 4, 2]
b = [9, 6, 2, 3, 8]
result = Hieu(a, b)
print(result)  # Kết quả: [1, 4, 5, 7]
