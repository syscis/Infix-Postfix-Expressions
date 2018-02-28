from infixToPostfix import infix_to_postfix
from cStack import Stack
from MixedFraction import MixedFraction

__author__ = 'Brad Miller and David Ranum\nModified by Hunt Blanchat'


def postfix_eval(postfix_expr):
    """ Takes a post fix expression and evaluates it using a helper function

    :param postfix_expr: postfix expression in form str
    :return: either an int or a float depending on inputs
    """
    operand_stack = Stack()
    token_list = postfix_expr.split()

    for token in token_list:
        try:
            float(token)
        except ValueError:
            operand2 = operand_stack.pop()
            operand1 = operand_stack.pop()
            result = do_math(token, operand1, operand2)
            operand_stack.push(result)

        else:
            try:
                int(token)
            except ValueError:
                operand_stack.push(float(token))
            else:
                operand_stack.push(int(token))
    return operand_stack.pop()


def do_math(op, op1, op2):
    """ Helper function for postfix that
    handles different operators and two ints/floats

    :param op: operator to be applied to op1 and op2
    :param op1: int or float
    :param op2: int or float
    :return: int or float
    """
    if op == "^":
        return op1 ** op2
    elif op == "*":
        return op1 * op2
    elif op == "/":
        return op1 / op2
    elif op == "+":
        return op1 + op2
    else:
        return op1 - op2


def eval_expression_file(file_name):
    """ Reads through a file of either infix or postfix expressions, determines
        which expression type is on a line and then evaluates the expression accordingly

    :param file_name: name of file being operated on
    :return:
    """
    print("\nEvaluation of {:}:".format(file_name))
    if file_name == 'fractionExpressions.txt':
        for line in open(file_name, 'r'):
            if line.strip() != '' and line.strip()[-1].isalnum():
                express = infix_to_postfix(line.strip())
                print('{:} = {:} = {:}'.format(line.strip(), MixedFraction(postfix_eval(express)), postfix_eval(express)))
            elif len(line.strip()) != 0:
                print('{:} = {:} = {:}'.format(line.strip(), MixedFraction(postfix_eval(express)), postfix_eval(line.strip())))
    else:
        for line in open(file_name, 'r'):
            if line.strip() != '' and line.strip()[-1].isalnum():
                express = infix_to_postfix(line.strip())
                print('{:} = {:}'.format(line.strip(), postfix_eval(express)))
            elif len(line.strip()) != 0:
                print('{:} = {:}'.format(line.strip(), postfix_eval(line.strip())))


def main():
    postfix_expressions = ['4.4 4.6 + 2 1 3 + / ^', '2 20 ^ 2 1 3 + / ^', '2 20 + 2 1 3 + + *', '2 -1 3 + -']
    infix_expressions = ["7 + 9 * 8 - 4 ^ 2", "7 + 9 * 8 / 4 ^ 2", "( 17 + 9 ) * 3 / ( 5 - 3 ) ^ 4",
                         "7.5 + 9 - 1.8 / 4 ^ 2.5"]
    print("\nEvaluation of postfix_expressions[]:")
    for item in postfix_expressions:
        print('{:} = {:,}'.format(item, postfix_eval(item)))
    print("\nEvaluation of infix_expressions[]:")
    for item in infix_expressions:
        express = infix_to_postfix(item)
        print('{:} = {:,}'.format(item, postfix_eval(express)))

    #print(postfix_eval("2 5 * 3 5 * 2 3 + / +"))
    #print(postfix_eval("2 5 * 3 5 * + 2 3 + /"))

    eval_expression_file('expressions.txt')
    eval_expression_file('fractionExpressions.txt')


if __name__ == '__main__':
    main()
