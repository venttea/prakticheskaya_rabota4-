words = ["яблоко", "банан", "киви", "голубика"]

sorted_words = sorted(words, key=lambda word: len(word))
print("Слова, отсортированные по длине: ", sorted_words)

num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_num = list(filter(lambda x: x % 2 == 0, num))
print("Четные числа: ", even_num)
