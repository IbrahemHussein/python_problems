def is_will_product(text):
    """Returns True if the given program is a will product
    parameter:
    program is a program that will  be checked if it produces or not

    """
    instruction = 'HQ9'
    for char in text:
        if char in instruction:
            return True

    return False


program = input()
if is_will_product(program):
    print('YES')
else:
    print('NO')
