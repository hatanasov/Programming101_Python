def count_substrings(haystack, needle):
    count = 0
    word_list = haystack.split()
    for word in word_list:
        if needle in word:
            count += 1
    return count


# print(count_substrings("Python is an awesome language to program in!", "o"))
# print(count_substrings("We have nothing in common!", "really?"))
# print(count_substrings("This is this and that is this", "this"))
# print(count_substrings("This is a test string", "is"))
