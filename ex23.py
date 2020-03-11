def copy_first_2_characters(str, n):
    new_str = ""
    for i in range(n):
        if len(str) <= 2:
            new_str = new_str + str
        else:
            new_str = new_str + str[:2]
    return new_str


print("Teste com oi", copy_first_2_characters("oi", 6))
print("Teste com tchau", copy_first_2_characters("tchau", 4))
