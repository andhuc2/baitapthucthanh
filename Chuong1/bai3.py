class GCD:
    @staticmethod
    def gcd_recursive(m, n):
        if n == 0:
            return m
        else:
            return GCD.gcd_recursive(n, m % n)

    @staticmethod
    def gcd_iterative(m, n):
        while n != 0:
            m, n = n, m % n
        return m

# Nhập vào hai số nguyên dương m và n
m = int(input("Nhập vào số nguyên dương m: "))
n = int(input("Nhập vào số nguyên dương n: "))

# Tìm ước số chung lớn nhất sử dụng phương thức đệ qui
gcd_recursive_result = GCD.gcd_recursive(m, n)
print("Ước số chung lớn nhất của", m, "và", n, "là (đệ qui):", gcd_recursive_result)

# Tìm ước số chung lớn nhất sử dụng phương thức không đệ qui
gcd_iterative_result = GCD.gcd_iterative(m, n)
print("Ước số chung lớn nhất của", m, "và", n, "là (không đệ qui):", gcd_iterative_result)
