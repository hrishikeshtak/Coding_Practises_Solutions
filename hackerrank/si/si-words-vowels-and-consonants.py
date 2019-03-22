#!/usr/bin/python3


def words_vowels_consonants(sentence):
    vowel_count = 0
    consonant_count = 0
    vowels = {'a', 'e', 'i', 'o', 'u'}
    word_count = len(sentence.split())
    for char in sentence:
        if char.lower() in vowels:
            vowel_count += 1
        elif char.lower() != ' ':
            consonant_count += 1
    print("%s %s %s" % (word_count, vowel_count, consonant_count))


if __name__ == '__main__':
    for _ in range(int(input())):
        sentence = input()
        words_vowels_consonants(sentence)
