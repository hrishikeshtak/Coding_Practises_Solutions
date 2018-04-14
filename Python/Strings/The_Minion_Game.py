#!/usr/bin/env python3

# Game Rules

# Both players are given the same string, S.
# Both players have to make substrings using the letters of the string S.
# Stuart has to make words starting with consonants.
# Kevin has to make words starting with vowels.
# The game ends when both players have made all possible substrings.

# A player gets +1 point for each occurrence of the substring in the string S.


def minion_game(string):
    # your code goes here
    vowels = ['A', 'E', 'I', 'O', 'U']
    Stuart = {}
    Kevin = {}
    for i in range(len(string)):
        for j in range(i, len(string)):
            if string[i] in vowels:
                if string[i:j+1] in Kevin.keys():
                    Kevin[string[i:j+1]] += 1
                else:
                    Kevin[string[i:j+1]] = 1
            else:
                if string[i:j+1] in Stuart.keys():
                    Stuart[string[i:j+1]] += 1
                else:
                    Stuart[string[i:j+1]] = 1
    # print("Stuart substrings with occurrence: ", Stuart)
    # print("Kevin substrings with occurrence: ", Kevin)
    Stuart_sum = sum(Stuart.values())
    Kevin_sum = sum(Kevin.values())
    if Stuart_sum > Kevin_sum:
        print("Stuart %s" % (Stuart_sum))
    elif Stuart_sum < Kevin_sum:
        print("Kevin %s" % (Kevin_sum))
    else:
        print("Draw")


if __name__ == '__main__':
    s = input()
    minion_game(s)
