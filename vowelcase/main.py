'''
1. make lowercase vowels uppercase
2. make uppercase consonants lowercase
'''

def vowel_case(string):

    vowels = ['a','e','i','o','u']
    consonants = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
    upper_consonants = [char.upper() for char in consonants]
    letters = []

    for letter in string:
        if letter in vowels:
            letters.append(letter.upper())
        elif letter in upper_consonants:
            letters.append(letter.lower())
        else:
            letters.append(letter)

    return ''.join(letters)

example_string = "vowelcase"

print(vowel_case(example_string))