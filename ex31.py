def gcd(int1, int2):
    divisor = 2
    divisor_array = []
    while (int1 > 1 and int2 > 1):
        if int1 % divisor == 0 and int2 % divisor == 0:
            int1 / divisor;
            int2 / divisor;
            divisor_array.extend(divisor)
            divisor = divisor + 1;
        elif int1 % divisor == 0:
            int1 / divisor;
