from test_framework import generic_test


def evaluate(expression: str) -> int:
    operations = "*+-/"
    stack = []
    
    expression = expression.split(",")
    for val in expression:
        if val in operations:
            right = stack.pop()
            left = stack.pop()
            if val == "+":
                stack.append(left+right)
            elif val == "-":
                stack.append(left-right)
            elif val == "*":
                stack.append(left*right)
            else:
                stack.append(left//right)
        else:
            stack.append(int(val))

    return stack[0]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('evaluate_rpn.py', 'evaluate_rpn.tsv',
                                       evaluate))
