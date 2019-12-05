def alphabet_filter(word):
    word_consonants = ""
    word_vowels = ""
    vowels = ["a","e","i","o","u"]
    for i in word:
        if i not in vowels:
            word_consonants += i
        else:
            word_vowels += i
            
           
    return word_consonants, word_vowels
   
    


print(alphabet_filter("codecool"))