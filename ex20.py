def multiply_string(str, number):
    new_string = ""
    for i in range(number):
        new_string = new_string + str
    return new_string

print(multiply_string("oi", 3))
