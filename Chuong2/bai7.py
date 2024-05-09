class Math:
    @staticmethod
    def Nhan(a, b):
        result = [0] * (len(a) + len(b))
        for i in range(len(a) - 1, -1, -1):
            for j in range(len(b) - 1, -1, -1):
                mul = int(a[i]) * int(b[j])
                pos1, pos2 = i + j, i + j + 1
                total = mul + result[pos2]
                result[pos1] += total // 10
                result[pos2] = total % 10
        if result[0] == 0:
            return result[1:]
        else:
            return result
