class FormulaError(Exception):
    pass

#to be used for in-class exercise
def parse_input(user_input):
    input_list = user_input.split()
    
    if len(input_list) != 3:
        raise FormulaError

    n1, op, n2 = input_list
    try: 
        n1 = float(n1)
        n2 = float(n2)
    except ValueError:
        raise FormulaError

    return n1, op, n2

def calculate(n1, op, n2): 
    if op == '+':
        return n1 + n2
    if op == '-':
        return n1 - n2
    if op == '*':
        return n1 * n2
    if op == '/':
        return n1 / n2
    else:
        raise FormulaError



while True:
    user_input = input('enter number, operator and another number: ')
    if user_input == 'quit':
        break
    
    n1, op, n2 = parse_input(user_input)
    result = calculate(n1, op, n2)
    print(result)

