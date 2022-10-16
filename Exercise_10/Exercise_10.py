"""
https://www.youtube.com/watch?v=MkgJfmN6dN8&list=PLu0W_9lII9agICnT8t4iYVSZ3eykIAOME&index=81&ab_channel=CodeWithHarry

Oh soldier prettify my folder

path, dictionary file, format

"""
import os
from os.path import isfile, isdir

def categorize_items(path, ignore_file, format_to_work):
    content = None
    with open(ignore_file) as f:
        content = f.read()
    ignore_list = content.split(",")
    
    all_items = {i: f"{path}\{i}" for i in os.listdir(path)}

    folders = {key: value for key, value in all_items.items() if isdir(value)}
    files = {key: value for key, value in all_items.items() if isfile(value) 
                and key.endswith(format_to_work) 
                and key not in ignore_list}
    perform_action(path, folders, files)


def perform_action(path, folders, files):
    for key, value in folders.items():
        os.rename(f"{path}\{key}", f"{path}\{str(key).capitalize()}")
    else:
        print("Folder renamed successfully..")
    
    index = 1
    for key, value in files.items():
        extension = str(key).split(".")[1]
        os.rename(f"{path}\{key}", f"{path}\{index}.{extension}")
        index += 1
    else:
        print("Files renamed successfully..")
    
def take_input():
    path = input("provide path: ")
    ignore_file = input("provide ignore file path: ")
    format_to_work = input("provide extension to work with: ")
    categorize_items(path, ignore_file, format_to_work)

take_input()

