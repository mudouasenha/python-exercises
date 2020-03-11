def concatenate_list_into_string(list):
    new_str = ""
    for item in list:
        new_str += str(item)
    return new_str

print(concatenate_list_into_string([3, "a", "b", "c"]))
