class Math:
    @staticmethod
    def Tru(a, b):
        result = []
        borrow = 0
        for i in range(len(a) - 1, -1, -1):
            digit_diff = int(a[i]) - int(b[i]) - borrow
            if digit_diff < 0:
                digit_diff += 10
                borrow = 1
            else:
                borrow = 0
            result.append(digit_diff)
        return result[::-1]
