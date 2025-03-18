words = ["peach", "apple", "grape", "kiwi", "banana"]
words.sort(key=lambda x : (len(x), x), reverse=True)
print(words)