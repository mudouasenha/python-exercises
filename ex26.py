def create_histogram(char, int_list):
    for num in int_list:
        output = ""
        for x in range(num):
            output += char
        print(output)


create_histogram("@", [ 3, 5, 2, 1 ])
