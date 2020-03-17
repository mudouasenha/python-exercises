def convert_time():
    days = int(input("Type Days : ")) * 24 * 3600
    hours = int(input("Type hours : ")) * 3600
    minutes = int(input("Type Minutes : ")) * 60
    seconds = int(input("Type seconds : "))
    
    sum = days + hours + minutes + seconds
    print("Seconds: ", sum)


convert_time()
