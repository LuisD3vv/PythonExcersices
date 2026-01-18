from collections import Counter


def stringCount(text):
    return Counter(text)


text = "Python Programming".lower().replace(" ","")
print(stringCount(text))