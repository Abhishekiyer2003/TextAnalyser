import re
inputfile=open("Demoanalyse")
def displaycontent():
    inputfile=open("Demoanalyse")
    print(inputfile.read())
def SearchText(text):

    with inputfile as f:
        for line_no,files in enumerate(f,start=1):
            if re.search(text, files):
                return f"Found the Text at {line_no}"
def Addtext(text):
    inputfile=open("Demoanalyse","a")
    with  inputfile as f:
        f.write(text)
        return f"Written"
def UpdateText(new_text):
    inputfile=open("Demoanalyse","w")












userText=input("Enter a text you want to search")
print(SearchText(userText))
text=input("Enter a text to be written")
print(Addtext(text))


