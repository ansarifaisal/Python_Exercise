"""
return a list indian phone number using regex

"""

import re
import os
from os.path import exists

path = input("Please enter path: ")

full_path = f"{os.getcwd()}\{path}"

if not exists(full_path):
    print("file doesn't exists")

matches = []
with open(full_path) as f:
    for num in f.readlines():
      x = re.match("^[6-9]{1}\d{9}$", num).string
      matches.append(x)

print(matches)
print("Ended.......")