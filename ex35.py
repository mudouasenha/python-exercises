def check_equal_or_sum(int1, int2):
    
    if int1 == int2 or abs(int1-int2) == 5 or (int1+int2) == 5:
        return True
    else:
        return False

print(check_equal_or_sum(7, 2))
print(check_equal_or_sum(3, 2))
print(check_equal_or_sum(2, 2))
print(check_equal_or_sum(199, 9))

