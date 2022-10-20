"""

Examples of palindrome includes 616, mom, 676, 100001

You have to take a number as an input from the user. You have to find the next palindrome corresponding
to that number. Your first input should be 'Number of test cases' and then take all the cases as input from
the user

Input:
3
451
10
2133

Output:

Next palindrome for 451 is 454
Next palindrome for 10 is 11
Next palindrome for 2133 is 2222

"""


def main():
    try:
        numbers = take_input()

        for i in numbers:
            print(f"Next palindrome for {i} is {next_palindrome(i)}")
    except Exception as e:
        print(e)


def next_palindrome(n):
    while not is_palindrome(n):
        n += 1
    return n


def is_palindrome(n):
    return True if str(n) == str(n)[::-1] else False


def take_input():
    element = int(input("Enter a number of cases: "))

    numbers = []

    for i in range(element):
        number = int(input(f"{i + 1}. "))
        numbers.append(number)

    return numbers


if __name__ == "__main__":
    main()

