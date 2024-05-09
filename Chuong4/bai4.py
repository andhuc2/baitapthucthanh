class Expression:
    @staticmethod
    def HauTo(expression):
        result = ''
        operators = []
        priority = {'+': 1, '-': 1, '*': 2, '/': 2}

        for char in expression:
            if char.isdigit():
                result += char + ' '
            elif char in priority:
                while operators and operators[-1] != '(' and priority[operators[-1]] >= priority[char]:
                    result += operators.pop() + ' '
                operators.append(char)
            elif char == '(':
                operators.append(char)
            elif char == ')':
                while operators[-1] != '(':
                    result += operators.pop() + ' '
                operators.pop()

        while operators:
            result += operators.pop() + ' '
        return result.strip()

# Sử dụng
expression = '2 + 3 * 5'
print(Expression.HauTo(expression))
