import pandas as pd

with open('textToInputBasic.txt', 'r') as file:
    text = file.read()
    result = set()
    for c in text:
        if 'א' <= c <= 'ת' or 'a' <= c <= 'z' or 'A' <= c <= 'Z':
            continue
        result.add(c)
    df = pd.DataFrame(result)
    df.to_excel("collect.xlsx")

