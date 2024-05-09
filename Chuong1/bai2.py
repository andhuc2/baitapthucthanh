class Neper:
    @staticmethod
    def factorial(n):
        if n == 0:
            return 1
        else:
            result = 1
            for i in range(1, n + 1):
                result *= i
            return result

    @staticmethod
    def neper_sum(n):
        total = 0
        for k in range(n + 1):
            total += 1 / Neper.factorial(k)
        return total

# Nhập vào số nguyên n
n = int(input("Nhập vào số nguyên n: "))
print("Tổng của các số hạng a0 + a1 + ... + an:", Neper.neper_sum(n))
