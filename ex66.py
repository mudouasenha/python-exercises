def imc():
    weight = float(input("Type your weight: "))
    height = float(input("Type your height: "))

    imc = round((weight / (height * height)), 2)

    print("Your IMC is ", imc)

imc()
