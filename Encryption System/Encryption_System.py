# coding: cp1251

def decimal_to_binary(input):
    result = ""
    while True:
        result += str(input % 2)
        input = int(input / 2)
        if input == 0:
            break
    return result [::-1]

print(decimal_to_binary(15))
