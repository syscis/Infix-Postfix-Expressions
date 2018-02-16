from cStack import Stack
from MixedFraction import MixedFraction

__author__ = "Brad Miller and David Ranum\nModified by Hunt Blanchat"


def infix_to_postfix(infixexpr):
    """ Takes a string of an expression in Infix form
        and returns a Postfix form expression

    :param infixexpr: expression in str
    :return: str in post fix form
    """

    prec = {}
    prec["^"] = 4
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    op_stack = Stack()
    postfix_list = []
    token_list = infixexpr.split()

    for token in token_list:
        try:
            float(token)
        except ValueError:
            if len(token) > 1 and token.__contains__('/'):
                postfix_list.append(str(float(MixedFraction.from_string(token))))
            elif token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
                postfix_list.append(token)
            elif token == '(':
                op_stack.push(token)
            elif token == ')':
                top_token = op_stack.pop()
                while top_token != '(':
                    postfix_list.append(top_token)
                    try:
                        top_token = op_stack.pop()
                    except AttributeError:
                        return "Bad Expression: {:}".format(' '.join(token_list))
                    else:
                        continue
            else:
                try:
                    (not op_stack.is_empty() and (prec[op_stack.peek()] >= prec[token]))
                except KeyError:
                    return "KeyError: '{:}' in {:}".format(token, ' '.join(token_list))
                else:
                    while (not op_stack.is_empty()) and \
                            (prec[op_stack.peek()] >= prec[token]):
                        postfix_list.append(op_stack.pop())
                    op_stack.push(token)
        else:
            postfix_list.append(token)

    while not op_stack.is_empty():
        postfix_list.append(op_stack.pop())
    return " ".join(postfix_list)


def main():
    print(infix_to_postfix("A * B + C ^ D"))
    print(infix_to_postfix("( 4.4 + 4.6 ) ^ ( 2 / ( 1 + 3 ) )"))
    print(infix_to_postfix("( 2 ^ 20 ) ^ ( 2 / ( 1 + 3 ) )"))
    print(infix_to_postfix("A * B ) + ( C ^ D )"))
    print(infix_to_postfix("( A * B ) + (C ^ D )"))
    print(infix_to_postfix("7 + 9 * 8 / 4 ^ 2"))
    print(infix_to_postfix("( 17 + 9 ) * 3 / ( 5 - 3 ) ^ 4"))
    print(infix_to_postfix("2 * 5 + 3 * 5 /  ( 2 + 3 )"))


if __name__ == '__main__':
    main()
