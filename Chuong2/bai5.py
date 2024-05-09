class Math:
    @staticmethod
    def Cong(a, b):
        result = []
        carry = 0
        if len(a) != len(b):
            return [-1] * max(len(a), len(b))
        for i in range(len(a) - 1, -1, -1):
            digit_sum = int(a[i]) + int(b[i]) + carry
            carry = digit_sum // 10
            result.append(digit_sum % 10)
        if carry:
            return [-1] * len(a)
        else:
            return result[::-1]
