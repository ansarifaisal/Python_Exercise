"""

    Catch the fraud

"""

import random


def main():
    take_input()


def take_input():
    user_input = int(input("Enter a number print the table: "))
    wrong_table = generate_wrong_table(user_input)
    wrong_index = validate_table(wrong_table, user_input)
    print(f"Index {wrong_index} in generated table is wrong")


def generate_wrong_table(num):
    table = [(i + 1) * num for i in range(10)]
    random_int = random.randint(2, 10)
    table[random_int] = random.randint(table[random_int - 1], table[random_int + 1])
    return table


def validate_table(wrong_table, num):
    table = [(i + 1) * num for i in range(10)]
    wrong_index = []
    for i in range(10):
        if wrong_table[i] != table[i]:
            wrong_index.append(i)
    return wrong_index


if __name__ == "__main__":
    main()
