class Fibonacci:
    @staticmethod
    def fibonacci_recursive(n):
        if n <= 1:
            return n
        else:
            return Fibonacci.fibonacci_recursive(n - 1) + Fibonacci.fibonacci_recursive(n - 2)

    @staticmethod
    def fibonacci_iterative(n):
        if n <= 1:
            return n
        else:
            a, b = 0, 1
            for _ in range(2, n + 1):
                a, b = b, a + b
            return b

# Sử dụng phương thức đệ qui để tính số Fibonacci của n
n = int(input("Nhập vào số nguyên n: "))
print("Số Fibonacci của", n, "là:", Fibonacci.fibonacci_recursive(n))

# Sử dụng phương thức không đệ qui để tính số Fibonacci của n
print("Số Fibonacci của", n, "là:", Fibonacci.fibonacci_iterative(n))
