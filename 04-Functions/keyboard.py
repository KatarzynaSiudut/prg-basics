###
# Functions to read any data type from the keyboard
#
def input_string(message):
    text = input(message)
    return text

def input_integer(message):
    number = input(message)
    return int(number)

def input_real(message):
    number = input(message)
    return float(number)

def input_boolean(message):
    answer = input(message)
    return answer.lower() == 'x'