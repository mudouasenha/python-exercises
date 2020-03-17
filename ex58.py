def sum_n_ints(n):
    summ = 0
    for x in range(n):
        summ = summ + x
        print(summ)
    return summ

print(sum_n_ints(5))


n = int(input("Type a number : "))
sum_num = (n * (n + 1)) / 2
print(sum_num)
