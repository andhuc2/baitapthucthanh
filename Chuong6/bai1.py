def Duynhat(arr):
    unique_arr = sorted(list(set(arr)))
    return unique_arr

# Sử dụng
arr = [1, 5, 3, 7, 5, 9, 7]
result = Duynhat(arr)
print(result)  # Kết quả: [1, 3, 5, 7, 9]
