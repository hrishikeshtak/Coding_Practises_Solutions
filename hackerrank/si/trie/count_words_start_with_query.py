#!/usr/bin/python3


class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.cnt = 0


def createNode():
    return TrieNode()


def insertTrie(root, word):
    cur = root
    for i in range(0, len(word)):
        idx = ord(word[i]) - ord('a')

        if cur.children[idx] is None:
            cur.children[idx] = createNode()
        cur = cur.children[idx]
        cur.cnt += 1
    return root


def search(root, w):
    cur = root
    for i in range(0, len(w)):
        idx = ord(w[i]) - ord('a')

        if cur.children[idx] is None:
            return 0

        cur = cur.children[idx]
    return cur.cnt


if __name__ == '__main__':
    query = ['da', 'ste', 'sma', 'dr']
    words = ['stem', 'dark', 'smart', 'smash', 'draw', 'dare']

    root = TrieNode()
    # import pdb; pdb.set_trace()
    for word in words:
        root = insertTrie(root, word)

    for q in query:
        cnt = search(root, q)
        print("query: %s, cnt: %s" % (q, cnt))
