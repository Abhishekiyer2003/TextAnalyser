import re

def SearchText(text):
    inputfile=open("Demoanalyse")
    with inputfile as f:
        for line_no,files in enumerate(f,start=1):
            if re.search(text, files):
                return f"Found the Text at {line_no}"

print(SearchText("Thank you"))

