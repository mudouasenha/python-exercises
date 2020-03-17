def feets_to_cm(ft):
    cm = ft * 30.48

    return cm

def inches_to_cm(inches):
    cm = inches * 2.54

    return cm

def get_size_in_cm():
    feet = int(input("Feet: "))
    inches = int(input("Inches: "))
    size = feets_to_cm(feet) + inches_to_cm(inches)

    return size

print(get_size_in_cm())
