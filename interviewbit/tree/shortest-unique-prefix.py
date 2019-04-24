#!/usr/bin/python3

"""
Input: [zebra, dog, duck, dove]
Output: {z, dog, du, dov}
where we can see that
zebra = z
dog = dog
duck = du
dove = dov
"""


class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.cnt = 0


class Solution:
    # @param A : list of strings
    # @return a list of strings
    def prefix(self, A):
        # First insert all the words in Trie
        root = TrieNode()
        # import pdb; pdb.set_trace()
        for word in A:
            root = self.insertTrie(root, word)

        res = []
        # Find prefix from cnt in Trie
        for word in A:
            res.append(self.prefixTrie(root, word))

        return res

    def insertTrie(self, root, word):
        if root is None:
            return None

        cur = root
        for char in word:
            idx = ord(char) - ord('a')
            if cur.children[idx] is None:
                cur.children[idx] = TrieNode()
            cur.cnt += 1
            cur = cur.children[idx]
        return root

    def prefixTrie(self, root, word):
        if root is None:
            return ""

        res = ""
        cur = root
        for char in word:
            idx = ord(char) - ord('a')
            if cur.children[idx]:
                if cur.cnt == 1:
                    break
                res += char
                cur = cur.children[idx]
        return res


if __name__ == '__main__':
    # Input = ["zebra", "dog", "duck", "dove"]
    Input = ["bearcat", "bert"]
    print(Solution().prefix(Input))
