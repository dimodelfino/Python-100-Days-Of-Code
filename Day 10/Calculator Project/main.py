from art import logo
operations = '+\n-\n*\n/'

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    if n2 == 0:
        print("Error: Cannot divide by zero.")
        return None
    return n1 / n2

calculations_dictionary = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def validate_number(value):
    is_valid = False
    while not is_valid:
        try:
            value = float(value)
            is_valid = True
        except ValueError:
            value = input('Invalid input. Please enter a valid integer \n')

    return value

def validate_operation(operation):
    while operation not in calculations_dictionary:
        operation = input("Invalid input. Please enter a valid operation. \n")
    return operation

flag = True
first_number = ''
result = ''
print(logo)
while flag:
    try:
        if first_number == '':
            first_number = validate_number(input("What's the first number? \n"))
        else:
            first_number = result
        print(operations)
        operation_selected = validate_operation(input("Pick an operation \n"))
        second_number = validate_number(input("What's the second number? \n"))
        result = calculations_dictionary[operation_selected](first_number, second_number)
        print(f'{first_number} {operation_selected} {second_number} = {result} \n')
        use_result = input(f'Type \'y\' to continue calculating with {result}, or type \'n\' to start a new calculation.\n').lower()
        if use_result == 'y':
            first_number = result
        elif use_result == 'n':
            first_number = ''
            print(logo)
        else:
            flag = False
    except ValueError:
        print("Invalid input.")

