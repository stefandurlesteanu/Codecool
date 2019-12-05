def english_word():
    return input("Provide english word: ")


def convert_to_present_participle(word):
    vowel = ["a","e","i","o","u"]
    if len(word) > 2:
        if word[-1] == 'e' and word[-2] != 'e':
            return word[:-1] + 'ing'
        elif word [-2:] == 'ie':
            return word[:-2] + 'ying'
        elif word[-3] not in vowel and word[-2] in vowel and word[-1] not in vowel:
            return word + word[-1] + 'ing'
        else:
            return word + 'ing'
    else:
        return word + 'ing'


def type_new_word(message):
    print(message)


def main():
    word = english_word()
    converted_word = convert_to_present_participle(word)
    type_new_word("Present participle form of {} is {}".format(word, converted_word))


if __name__ == "__main__":
    main()