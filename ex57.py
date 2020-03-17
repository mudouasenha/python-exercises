import timeit

def calc():
    x = 4.565545
    y = 133231

    for x  in range(100):
        x = x + 1

    return x

#print(timeit.timeit(calc, number=100000))


import time
def sum_of_n_numbers(n):
    start_time = time.time()
    s = 0
    for i in range(1,n+1):
        s = s + i
    end_time = time.time()
    return s,end_time-start_time

n = 5
print("\nTime to sum of 1 to ",n," and required time to calculate is :",sum_of_n_numbers(n))
