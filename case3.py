n = int(input("Enter size of diamond (1 to 9): "))

if n < 1 or n > 9:
    print("Invalid dimension. Enter a value between 1 and 9.")
else:
    for i in range(1, 2 * n):
        if i <= n:
            k = i
        else:
            k = 2 * n - i
        line = " " * (n - k)
        if k == 1:
            line = line + "1"
        else:
            line = line + str(k) + " " * (2 * k - 3) + str(k)
        print(line)
