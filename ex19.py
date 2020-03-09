def concatenate_is_in_string(str):
    if len(str) > 2 and str[:2] == "Is":
        return str
    return "Is" + str


print(concatenate_is_in_string("Array"))
print(concatenate_is_in_string("IsEmpty"))
