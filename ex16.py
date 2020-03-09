def number_less_17(number):
    if number > 17:
        return (number - 17) * 2
    else:
        return 17 - number

print("Maior", number_less_17(20))
print("Menor", number_less_17(15))
print("igual", number_less_17(17))
