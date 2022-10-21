"""

    You are given few sentences as a list (python list of sentences). Take a query string as an input from the
    user. You have to pull out the sentences matching this query provided by the user in decreasing order of
    relevance after converting every word in the query and the sentence to lowercase. Most relevant
    sentence is the one with the maximum number of matching words with the query.

    Sentences = ["This is good", "Python is good", "Python is not python snake"]

    input:
    Please input your query string
    "Python is"

    output:
    3 results found:
    1. python is not python snake
    2. python is good
    3. this is good

"""

import re


def main():
    take_input()


def take_input():
    user_input = input("Please input your query string: ")
    data_set = ["This is good", "Python is good", "Python is not python snake"]

    filtered_data_set = {f"{i}": len(list(re.finditer(user_input, str(i).lower()))) for i in data_set
                         if len(list(re.finditer(user_input, str(i).lower()))) > 0}

    sorted_filtered_data_set = dict(sorted(filtered_data_set.items(), reverse=True))
    num = 0
    for i in sorted_filtered_data_set:
        num += 1
        print(f"{num}. {i}")


if __name__ == "__main__":
    main()
