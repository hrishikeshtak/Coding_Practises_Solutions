#!/usr/bin/python3

# No Prefix Set


class TrieNode:
    def __init__(self):
        self.children = [None] * 12
        self.flag = False  # To identify prefix


def createNode():
    return TrieNode()


def addName(root, word):
    cur = root
    for i in range(0, len(word)):
        idx = ord(word[i]) - ord('a')

        if cur.children[idx] is None:
            cur.children[idx] = createNode()
        cur = cur.children[idx]

    cur.flag = True
    return root


def search(root, w):
    cur = root
    for i in range(0, len(w)):
        idx = ord(w[i]) - ord('a')

        if cur.children[idx] is None:
            return False

        cur = cur.children[idx]

        # Find prefix for query
        if cur.flag:
            return True

    return True


if __name__ == '__main__':
    status = False
    root = TrieNode()
    for _ in range(int(input())):
        name = input()
        status = search(root, name)
        if status:
            print("BAD SET")
            print(name)
            break

        root = addName(root, name)

    if not status:
        print("GOOD SET")
