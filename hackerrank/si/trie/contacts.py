#!/usr/bin/python3

# Contacts application!


class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.cnt = 0


def createNode():
    return TrieNode()


def addName(root, word):
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
    root = TrieNode()
    for _ in range(int(input())):
        op, name = input().split()

        if op.lower() == 'add':
            root = addName(root, name)
        else:
            cnt = search(root, name)
            print(cnt)
            # print("query: %s, cnt: %s" % (name, cnt))
