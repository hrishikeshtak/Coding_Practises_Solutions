#!/usr/bin/python3

from collections import defaultdict


class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isWord = False


class Solution:
    # @param A : string
    # @param B : list of strings
    # @return a list of integers
    def solve(self, A, B):
        root = TrieNode()
        for word in A.split("_"):
            root = self.insertTrie(root, word)

        counter = defaultdict(lambda: 0)

        for i in range(0, len(B)):
            counter[i] = 0
            for word in B[i].split("_"):
                if self.searchTrie(root, word):
                    counter[i] += 1
        # counter.s
        counter = sorted(counter.items(), key=lambda x: x[1], reverse=True)
        # print(counter)
        res = []
        for k, v in counter:
            res.append(k)
        return res

    def searchTrie(self, root, word):
        cur = root
        if cur is None:
            return False

        for char in word:
            idx = ord(char) - ord('a')
            if cur.children[idx] is None:
                return False
            cur = cur.children[idx]
        return cur.isWord

    def insertTrie(self, root, word):
        cur = root
        for char in word:
            idx = ord(char) - ord('a')
            if cur.children[idx] is None:
                cur.children[idx] = TrieNode()
            cur = cur.children[idx]
        cur.isWord = True
        return root


if __name__ == '__main__':
    # S : A string S containing "Good Words" separated by  "_" character.
    # R : A vector of strings containing Hotel Reviews. Review strings are also
    # separated by "_" character.
    # S = "cool_ice_wifi"
    # R = ["water_is_cool", "cold_ice_drink", "cool_wifi_speed"]
    S = "play_boy"
    R = ["smart_guy", "girl_and_boy_play", "play_ground"]
    print(Solution().solve(S, R))
