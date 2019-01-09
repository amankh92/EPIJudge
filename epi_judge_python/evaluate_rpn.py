from test_framework import generic_test


def evaluate(expression):
    stack = []
    oper = {"+": lambda y, x: x + y,
            "-": lambda y, x: x - y,
            "*": lambda y, x: x * y,
            "/": lambda y, x: x // y}
    for char in expression.split(','):
        if char.isdigit():
            stack.append(int(char))
        else:
            stack.append(oper[char](stack.pop(), stack.pop()))
    # TODO - you fill in here.
    return stack.pop()


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("evaluate_rpn.py", 'evaluate_rpn.tsv',
                                       evaluate))
