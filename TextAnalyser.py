import re
import os
FileName="Demoanalyse"
def displaycontent():
    print(FileName.read())
def SearchText(text):
    with open(FileName) as f:
        for line_no,files in enumerate(f,start=1):
            if re.search(text, files):
                return f"Found the Text at {line_no}"
def Addtext(text):
    with  open(FileName,"a") as f:
        f.write(text)
        return f"Written"
def DeleteText(text):
    with open(FileName, "r") as f:
        content = f.read()

    # Remove all occurrences of the word
    new_content = re.sub(text, "", content)

    with open(FileName, "w") as f:
        f.write(new_content)

    return "Text deleted successfully"












userText=input("Enter a text you want to search")
print(SearchText(userText))
text=input("Enter a text to be written")
print(Addtext(text))
print(DeleteText(text))


