
start = int(input("Starting weekday (0=Mon ... 6=Sun): "))
days = int(input("Number of days in month (28-31): "))

if start < 0 or start > 6 or days < 28 or days > 31:
    print("Invalid input")
else:
    print("Mo Tu We Th Fr Sa Su")
    line = "   " * start
    col = start
    for d in range(1, days + 1):
        line = line + str(d).rjust(2) + " "
        col = col + 1
        if col == 7:
            print(line)
            line = ""
            col = 0
    if col != 0:
        print(line)
