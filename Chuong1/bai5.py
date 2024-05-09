class Number:
    @staticmethod
    def classify_number(n):
        divisor_sum = sum([i for i in range(1, n) if n % i == 0])
        if divisor_sum < n:
            return "deficient"
        elif divisor_sum == n:
            return "perfect"
        else:
            return "abundant"

    @staticmethod
    def classify_numbers_in_range(x, y):
        for num in range(x, y + 1):
            print(f"Số {num} là {Number.classify_number(num)}.")

# Nhập vào hai số nguyên dương x và y với x ≤ y
x = int(input("Nhập vào số nguyên dương x: "))
y = int(input("Nhập vào số nguyên dương y (y ≥ x): "))

# Phân loại các số từ x đến y và in kết quả
Number.classify_numbers_in_range(x, y)
