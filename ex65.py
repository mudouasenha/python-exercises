def convert_seconds():
    seconds  = int(input("Type seconds: "))
    days = round(seconds / (24 * 3600))
    seconds = seconds % (24 * 3600)
    hours = round(seconds / 3600)
    seconds = seconds % 3600
    minutes = round(seconds / 60)
    seconds = seconds % 60

    print("Days: ", days)
    print("Hours", hours)
    print("Minutes: ", minutes)
    print("Seconds: ", seconds)

convert_seconds()

