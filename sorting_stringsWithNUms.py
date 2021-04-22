sentence = "is2 Thi1s T4est 3a"

sorted_string = []
split_sentence = sentence.split()

for i in range(1,len(split_sentence) + 1):
    for word in split_sentence:
        for w in word:

            if str(i) == w:
                sorted_string.append(word)

print(' '.join(sorted_string))