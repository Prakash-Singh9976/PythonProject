''' Write a code which accepts a sequence of words as input and prints the words in a sequence after sorting them alphabetically '''

def sorted_Words_Alphabettically(words):
    word_list = sorted(words)
    return word_list


words = input("Enter words sequentially : ")

wordsLists = words.split()
sorted_Words_list = sorted_Words_Alphabettically(wordsLists)

print("Words in sorted order : "+" ".join(sorted_Words_list))