
"""
    Enter a number and check in the range if the numbers in the range are the divisor of the number provided

"""
try:
    n = int(input("Enter numbers of apple harry has got: "))
    mn = int(input("Enter mn: "))
    mx = int(input("Enter mx: "))
except Exception as e:
    print(e)

for i in range(mn, mx + 1):
    if n % i == 0:
        print(f"{i} is a divisor of {n}")
    else:
        print(f"{i} is a not divisor of {n}")
