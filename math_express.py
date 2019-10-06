"""
mathExpress
A simple mathematical expressions generator/solver

"""

import itertools


def expression_solver(express):

    """
    Parameters:
    express (string): The generated expression that should be solved

    Returns:
    int: The expression solution
    """

    expression = express[:]
    res_index = 0  # Final result position in list
    for index in range(len(expression)):
        left = 1
        right = 1
        if expression[index] == '*':
            while expression[index-left] == '':
                left += 1
            while expression[index+right] == '':
                right += 1
            expression[index] = (expression[index-left] *
                                 expression[index+right])
            expression[index-left] = ''
            expression[index+right] = ''
            res_index = index
        elif expression[index] == '/':
            while expression[index-left] == '':
                left += 1
            while expression[index+right] == '':
                right += 1
            expression[index] = (expression[index-left] /
                                 expression[index+right])
            expression[index-left] = ''
            expression[index+right] = ''
            res_index = index
    for index in range(len(expression)):
        left = 1
        right = 1
        if expression[index] == '+':
            while expression[index-left] == '':
                left += 1
            while expression[index+right] == '':
                right += 1
            expression[index] = (expression[index-left] +
                                 expression[index+right])
            expression[index-left] = ''
            expression[index+right] = ''
            res_index = index
        elif expression[index] == '-':
            while expression[index-left] == '':
                left += 1
            while expression[index+right] == '':
                right += 1
            expression[index] = (expression[index-left] -
                                 expression[index+right])
            expression[index-left] = ''
            expression[index+right] = ''
            res_index = index
    return expression[res_index]


def expression_finder(numbers, operators, exp_res):

    """
    Parameters:
    numbers (list of ints): Numbers that should appear in the expression
    exp_res (int): Expected result for the expression
    operators (list of chars): Operators tha should appear in the expression

    Returns:
    list of strings: A list of the possible expressions
    """

    # Make all possible ordered lists of numbers chosen from numbers list
    possible_num = list(itertools.permutations(numbers))
    # Make all possible ordered lists of operations chosen from operations list
    possible_op = list(itertools.product(operators, repeat=(len(numbers)-1)))
    expressions = []
    for num in possible_num:
        for op in possible_op:
            expr = []
            expr.append(num[0])
            for i in range(len(op)):
                expr.append(op[i])  # Add operator
                expr.append(num[i+1])  # Add number
            if expression_solver(expr) == exp_res:
                expressions.append(str(expr)
                                   .replace(',', '')
                                   .replace("'", '')
                                   .replace('[', '')
                                   .replace(']', ''))
    return expressions


numbers = [2, 4, 5, 10, 12]
operators = ['+', '*', '-']
expected_res = 22
print(expression_finder(numbers, operators, expected_res))
