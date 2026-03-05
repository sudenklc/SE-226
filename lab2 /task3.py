n = int(input("Enter a positive integer between 3 and 9 inclusive: "))

while n < 3 or n > 9:
    print("Invalid number. Please enter a number between 3 and 9.")
    n = int(input("Please enter a number between 3 and 9: "))

for i in range(1, 2 * n):
    k = n - abs(n - i)

    for j in range(k):
        print("*", end=" ")

    print()
