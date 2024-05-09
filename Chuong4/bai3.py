class Expression:
    @staticmethod
    def GiaTri(expression):
        operands = []
        operators = []
        priority = {'+': 1, '-': 1, '*': 2, '/': 2}

        def evaluate(op1, op2, operator):
            if operator == '+':
                return op1 + op2
            elif operator == '-':
                return op1 - op2
            elif operator == '*':
                return op1 * op2
            elif operator == '/':
                return op1 / op2

        def apply_operator():
            op2 = operands.pop()
            op1 = operands.pop()
            operator = operators.pop()
            operands.append(evaluate(op1, op2, operator))

        i = 0
        while i < len(expression):
            if expression[i].isdigit():
                operand = ''
                while i < len(expression) and expression[i].isdigit():
                    operand += expression[i]
                    i += 1
                operands.append(int(operand))
            elif expression[i] in priority:
                while operators and priority[operators[-1]] >= priority[expression[i]]:
                    apply_operator()
                operators.append(expression[i])
                i += 1
            elif expression[i] == '(':
                operators.append('(')
                i += 1
            elif expression[i] == ')':
                while operators[-1] != '(':
                    apply_operator()
                operators.pop()
                i += 1
        while operators:
            apply_operator()
        return operands[0]

# Sử dụng
expression = '2 + 3 * 5'
print(Expression.GiaTri(expression))
