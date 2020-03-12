def sum_different_numbers(int1, int2, int3):
    if int1 == int2 or int2 == int3:
        sum = 0
    else:
        sum =int1 + int2 + int3
    return sum

print(sum_different_numbers(1, 4, 8))
print(sum_different_numbers(2, 2, 7))
