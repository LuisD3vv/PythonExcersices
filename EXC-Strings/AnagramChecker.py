def anagramChecker(texta,textb):
    if sorted(texta,reverse=True) == sorted(textb,reverse=True):
        return True
    return False

word1 = "listes"
word2 = "silent"
print(f"Is '{word1}' an anagram of '{word2}'?: {anagramChecker(word1,word2)}")

e