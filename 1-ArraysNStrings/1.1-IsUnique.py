def is_unique(word):
    word_set = set()

    for x in word:
        if x not in word_set:
            word_set.add(x)
        else:
            return False

    return True

# still need to review below method
def is_unique_wo_storage(word):
    for i in range(len(word)):
        c = word[i]
        for j in range(i+1, len(word)):
            if c == word[j]:
                return False

    return True



""" Driver code """
word = 'Unique word '

print(is_unique(word))
print(is_unique_wo_storage(word))
