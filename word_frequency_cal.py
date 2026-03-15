sentence = input("enter the sentence to calculate the words in it :" )

word = sentence.split()

freq = {}

for words in word:
    if words in freq:
        freq[words] +=  1
    else:
        freq[words] = 1

print(freq)

