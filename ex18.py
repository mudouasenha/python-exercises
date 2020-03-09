def sum_three_numbers(num1, num2, num3):
    if num1 == num2 and num2 == num3:
        return (num1 + num2 + num3) ** 3
    else:
        return num1 + num2 + num3

print("Equals", sum_three_numbers(3, 3, 3))
print("Different", sum_three_numbers(3, 4, 5))
