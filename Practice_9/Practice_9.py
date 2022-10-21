
import random


def main():
    try:
        take_input()
    except Exception as e:
        print(e)


def take_input():
    no_of_element = int(input("Enter number of elements: "))
    names = []
    for i in range(no_of_element):
        name = input(f"{i + 1}. Enter first name and last name: ")

        if name.find(" ") == -1:
            print("Invalid Input! Name should have space.")
            continue

        if name.isspace():
            print("Invalid Input! Only spaces detected")
            continue

        names.append(name)

    if len(names) <= 0:
        raise Exception("Elements not found in the list")

    first_names = [i[0: i.find(" ")] for i in names]
    last_names = [i[i.find(" ") + 1: len(i)] for i in names]
    random_names = gen_random_name(first_names, last_names)
    print(f"Random Names Are - {random_names}")


def gen_random_name(first_names, last_names):
    total_len = len(first_names)
    random_names = []
    for i in range(total_len):
        first_name_random = random.randint(0, total_len - 1)
        last_name_random = random.randint(0, total_len - 1)
        random_names.append(f"{first_names[first_name_random]} {last_names[last_name_random]}")
    return random_names


if __name__ == "__main__":
    main()
