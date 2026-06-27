import re
import os

FileName = "C:\Pythonprojects\Demoanalyse"


def displaycontent():
    try:
        with open(FileName, "r") as f:
            print(f.read())
    except FileNotFoundError:
        print("File not found")

dsa
def SearchText(text):
    try:
        with open(FileName, "r") as f:
            found = False
            for line_no, line in enumerate(f, start=1):
                if re.search(re.escape(text), line):
                    print(f"Found at line {line_no}")
                    found = True

            if not found:
                print("Text not found")
    except FileNotFoundError:
        print("File not found")


def Addtext(text):
    with open(FileName, "a") as f:
        f.write(text + "\n")
    print("Written Successfully")


def DeleteText(text):
    try:
        with open(FileName, "r") as f:
            content = f.read()

        new_content = re.sub(re.escape(text), "", content)

        with open(FileName, "w") as f:
            f.write(new_content)

        print("Text deleted successfully")

    except FileNotFoundError:
        print("File not found")


while True:
    print("\n------TEXT ANALYZER------")
    print("1.GET THE FILE")
    print("2.SEARCH FOR A TEXT")
    print("3.ADD A TEXT")
    print("4.DELETE A TEXT")
    print("5.EXIT")

    operations = int(input("Enter your choice: "))

    match operations:

        case 1:
            displaycontent()

        case 2:
            user_text = input("Enter text to search: ")
            SearchText(user_text)

        case 3:
            user_text = input("Enter text to add: ")
            Addtext(user_text)

        case 4:
            user_text = input("Enter text to delete: ")
            DeleteText(user_text)

        case 5:
            print("Thank You!")
            break

        case _:
            print("Invalid Choice")