def check_list_contains_value(value_list, number):
    for value in value_list:
        if number == value:
            return True
    return False


print("1", check_list_contains_value([ 1, 5, 8, 3 ], 1))
print("7", check_list_contains_value([ 1, 5, 8, 3 ], 7))
