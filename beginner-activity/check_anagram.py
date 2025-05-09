def check_anagram(word1, word2):
    word1 = word1.lower()
    word2 = word2.lower()
    return sorted(word1) == sorted(word2)

word1 = input("Enter a string: ")
word2 = input("Enter a string: ")

print("Anagram is", check_anagram(word1, word2))