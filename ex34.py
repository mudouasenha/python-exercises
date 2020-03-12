def sum_two_differents(int1, int2):
    sum = int1 + int2
    if sum >= 15 and sum <= 20:
        sum = 20
    
    return sum


print(sum_two_differents(1, 12))
print(sum_two_differents(1, 16))
