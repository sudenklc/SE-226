n = int(input("Enter a positive integer between 3 and 9 inclusive: "))

for i in range(1, 2 * n):
    k = n - abs(n - i)

    for j in range(k):
        print("*", end=" ")

    print()
