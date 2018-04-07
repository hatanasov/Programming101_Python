def anagrams():
    word = [''.join(w.split('_')) for w in input().split()]
    first_word = sorted([char.lower() for char in word[0]])
    second_word = sorted([char.lower() for char in word[1]])
    if first_word == second_word:
        return 'ANAGRAMS'
    else:
        return 'NOT ANAGRAMS'

print(anagrams())