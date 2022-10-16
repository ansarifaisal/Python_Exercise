"""

Coroutine Excercise

Read 15 files and try to find which file contains the your name or the search phrase.

"""
import os

data = {}
files = {}

def read_files():
    """
        This method will read the text file available in the directory
    """
    print("File reading starts")
    global data, files

    dir_path = "F:\Practice\BasicPython\Exercise_9\Data"
    files = {i: f"{dir_path}\{i}" for i in os.listdir(dir_path) if i.endswith(".txt")}

    if len(files) == 0:
        print("no file found")
        return None

    for key, value in files.items():
        with open(value, "r+") as f:
            data[key] = f.read()

    print("File read successfully!")

def searcher():
    """
        This is the search method which uses coroutine to search text from a file.
    """
    read_files()
    
    while True:
        text = (yield)
        for key, value in data.items():
            if text in value:
                print(f"{text} found in {key}")

try:
    search = searcher()
    next(search) # coroutine intialized
    search.send("Lorem") # Text to search from the files
    search.close() # closing the coroutine to release the resources
except Exception as ex:
    print(ex)