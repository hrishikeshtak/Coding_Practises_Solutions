from sys import stdin, stdout


class Heap:
    # Implement Min Heap using 1 based index
    arr = [None]

    def __init__(self, heap_type="min"):
        self.heap_type = heap_type

    def size(self):
        return len(self.arr) - 1

    def insert(self, key):
        self.arr.append(key)
        # print(self.arr)

        # after addition, check heap property
        idx = self.size()

        while idx > 1 and self.arr[idx] < self.arr[idx//2]:
            self.arr[idx], self.arr[idx//2] = self.arr[idx//2], self.arr[idx]
            idx = idx // 2
        # print(self.arr)

    def getMin(self):
        N = self.size()
        if N == 0:
            # print("Empty")
            stdout.write(str("Empty") + "\n")
        else:
            # print(self.arr[1])
            stdout.write(str(self.arr[1]) + "\n")

    def LeftChildren(self, i):
        left = 2 * i
        if left >= self.size():
            return -1

        return left

    def RightChildren(self, i):
        right = 2 * i + 1
        if right >= self.size():
            return -1

        return right

    def delMin(self):
        # print("before delMin: ")
        # print(self.arr)

        # copy last element to 1st element and then maintain heap property
        N = self.size()
        if N == 0:
            return
        elif N == 1:
            _ = self.arr.pop()
            return

        self.arr[1] = self.arr.pop()
        self.heapify_iterative(1)
        # self.heapify_recursive(1)
        # print("After delMin: ")
        # print(self.arr)

    def heapify_iterative(self, idx):
        left = self.LeftChildren(idx)
        right = self.RightChildren(idx)

        while left != -1 or right != -1:
            # find smallest index value from l and r
            smallest = idx
            if left != -1 and self.arr[left] < self.arr[smallest]:
                smallest = left
            if right != -1 and self.arr[right] < self.arr[smallest]:
                smallest = right

            if smallest != idx:
                self.arr[idx], self.arr[smallest] = self.arr[smallest], \
                    self.arr[idx]
                break
            idx = smallest
            left = self.LeftChildren(idx)
            right = self.RightChildren(idx)

    def heapify_recursive(self, idx):
        smallest = idx
        left = self.LeftChildren(idx)
        right = self.RightChildren(idx)

        # find min index from l and r
        if left != -1 and self.arr[left] < self.arr[smallest]:
            smallest = left
        if right != -1 and self.arr[right] < self.arr[smallest]:
            smallest = right

        if smallest != idx:
            self.arr[idx], self.arr[smallest] = self.arr[smallest], \
                self.arr[idx]
            self.heapify_recursive(smallest)


def implementHeap(heap, op):
    if op[0].lower().rstrip() == "insert":
        x = int(op[1].rstrip())
        heap.insert(x)

    elif op[0].rstrip().lower() == "getmin":
        heap.getMin()

    elif op[0].rstrip().lower() == "delmin":
        heap.delMin()
    else:
        print("Invalid Operation")
        return


if __name__ == '__main__':
    heap = Heap()
    for _ in range(int(input())):
        op = stdin.readline().split(" ", 1)
        # print(op)
        implementHeap(heap, op)
