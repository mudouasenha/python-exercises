def count_4_in_list(list):
    count = 0
    for number in list:
        if number == 4:
            count = count + 1;
    return count;

test_list = [ 1, 2, 3, 4, 7, 4, 4, 7, 4 ]

print("Counted 4's", count_4_in_list(test_list))
