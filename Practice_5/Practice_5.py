"""

    You are given a list which contains some numbers. You have to print a list of next palindromes only if the
    number is greater than 10 otherwise you will print that number

"""


def main():
    try:
        numbers = take_input()
        print(numbers)
        palindromes = []
        for i in numbers:
            palindromes.append(next_palindrome(i))

        print(palindromes)
    except Exception as e:
        print(e)


def next_palindrome(n):
    if n <= 10:
        return n
    while not is_palindrome(n):
        n += 1
    return n


def is_palindrome(n):
    return True if str(n) == str(n)[::-1] else False


def take_input():
    element = int(input("Number of element you want to enter: "))
    numbers = []
    for i in range(element):
        number = int(input(f"{i}. "))
        numbers.append(number)
    return numbers


if __name__ == "__main__":
    main()
