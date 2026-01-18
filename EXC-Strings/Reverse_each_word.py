'''
Practice Problem: Given a sentence, reverse each individual word within the string while maintaining the original word order
'''
def ReverseWords(input_text):
    splittext = input_text.split(" ")
    x = [x[::-1] for x in splittext] # hermoso
    return x

text = "Python is awesome"
#result = ReverseWords(text)
#print(f"original Word '{text}'")
#print(f"Reversed words '{" ".join(result)}'")]


def PalindromeSentence(input_text):
    clean_text = []
    for x in input_text.lower().strip():
        if x.isalnum():
            clean_text.append(x)
    text_var = "".join(clean_text)
    reverse_text = text_var[::-1]   
    if text_var == reverse_text:
        return True
    return False

given_text = "yo hago yoga hoy"
print(f"Is '{given_text}' a palindrome sentence ?: {PalindromeSentence(given_text)}")


# 80 - 20

# se aprende mejor aplicando y reconociendo los errores