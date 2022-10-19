
"""
    Reverse a list with the following method:
    1. Inbuilt method of python
    2. Listname[::-1] slicing trick
    3. Swapping first element with last one and second element with the second last element and so on..

"""


def main_method():

    number_of_element = int(input("Provide the number of element you want to enter: "))
    user_input = []
    for i in range(number_of_element):
        ele = int(input(f"{i + 1}. "))
        user_input.append(ele)

    print(f"Entered list   - {user_input}")
    temp_list = user_input.copy()
    temp_list.reverse()
    print(f"inbuilt method - {temp_list}")

    temp_list = user_input.copy()
    slicing_trick = temp_list[::-1]
    print(f"slice method   - {slicing_trick}")

    temp_list = user_input.copy()

    for i in range(int(len(temp_list)/2)):
        temp = temp_list[i]
        temp_list[i] = temp_list[(len(temp_list) - i) - 1]
        temp_list[(len(temp_list) - i) - 1] = temp

    print(f"Swap method    - {temp_list}")


if __name__ == "__main__":
    main_method()
