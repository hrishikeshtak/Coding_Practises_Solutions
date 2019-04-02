#!/usr/bin/python3


def reverse_word(reverse_sentence):
    p1 = 0
    p2 = 0
    for i in range(0, len(reverse_sentence)):
        if reverse_sentence[p2] != " ":
            p2 += 1
        elif reverse_sentence[p2] == " ":
            k = p2 - 1
            while p1 <= k:
                reverse_sentence[p1], reverse_sentence[k] = \
                    reverse_sentence[k], reverse_sentence[p1]
                p1 += 1
                k -= 1
            p2 += 1
            p1 = p2
        # last word
        if p2 == len(reverse_sentence):
            k = p2 - 1
            while p1 <= k:
                reverse_sentence[p1], reverse_sentence[k] = \
                    reverse_sentence[k], reverse_sentence[p1]
                p1 += 1
                k -= 1
    # print(reverse_sentence)
    return reverse_sentence


def reverse_the_sentence(sentence):
    # print(sentence)
    reverse_sentence = list(sentence)
    # print(reverse_sentence)
    p1 = 0
    p2 = len(reverse_sentence) - 1
    while p1 < p2:
        reverse_sentence[p1], reverse_sentence[p2] = \
            reverse_sentence[p2], reverse_sentence[p1]
        p1 += 1
        p2 -= 1
    # print(reverse_sentence)
    reverse_sentence = reverse_word(reverse_sentence)
    print("".join(reverse_sentence))


if __name__ == '__main__':
    for _ in range(int(input())):
        sentence = input()
        reverse_the_sentence(sentence)
