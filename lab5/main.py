def factorial(x):
    if x == 0 or x == 1:
        return 1
    else:
        return x * factorial(x-1)


e = lambda x, n: (x ** n) / factorial(n)

def exp_x(x, n):
    total = 0
    i = 0
    while i <= n:
        total = total + e(x, i)
        i += 1

    return total


def series(n):
    """
    My function calls itself recursively. It takes "n" as a parameter and n is zero is our base case. It saves the result
    into a global variable that stays updated. Every time the function runs, it checks the current value of n. If n is odd,
    it calculates 1/n and adds that amount to the global result. If n is even, it, again, calculates 1/n but subtracts it
    from the global result rather than adding it. After calculating current n, the function calls itself again but with n-1
    to move to next step. It repeats until n is zero. Then it stops running.

    """
    global result

    if n == 0:
        return

    if n % 2 == 0:
        result = result - (1 / n)
    else:
        result = result + (1 / n)

    series(n - 1)

x = float(input("Enter x value for e^x: "))
n1 = int(input("Enter number of terms for e^x: "))

print("e^x approximation:", exp_x(x, n1))


n2 = int(input("Enter n value for the series: "))

result = 0
series(n2)

print("Series result:", result)
