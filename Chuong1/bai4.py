class Pascal:
    @staticmethod
    def pascal_triangle(n):
        for line in range(0, n):
            for i in range(0, line + 1):
                print(Pascal.binomial_coefficient(line, i), end=" ")
            print()

    @staticmethod
    def binomial_coefficient(n, k):
        res = 1
        if k > n - k:
            k = n - k
        for i in range(k):
            res *= (n - i)
            res //= (i + 1)
        return res

# Nhập vào số nguyên dương n
n = int(input("Nhập vào số nguyên dương n: "))

# In ra tam giác Pascal ứng với bậc n
Pascal.pascal_triangle(n)
