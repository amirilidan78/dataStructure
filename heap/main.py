# Python MaxHeap
# public functions: push, peek, pop
# private functions: __swap, __floatUp, __bubbleDown
import ctypes
class MaxHeap:
    def __init__(self, items=[]):
        super().__init__()
        self.heap = [0]
        for i in items:
            self.heap.append(i)
            self.__floatUp(len(self.heap) - 1)


    def push(self, data):
        self.heap.append(data)
        self.__floatUp(len(self.heap) - 1)

    # return root and delete root
    def peek(self):
        if self.heap[1]:
            return self.heap[1]
        else:
            return False

    # swap root to the alst element and delete it
    def pop(self):
        if len(self.heap) > 2:
            self.__swap(1, len(self.heap) - 1)
            max = self.heap.pop()
            self.__bubbleDown(1)
        elif len(self.heap) == 2:
            max = self.heap.pop()
        else:
            max = False
        return max

    def __swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def __floatUp(self, index):
        parent = index // 2
        if index <= 1:
            return
        elif self.heap[index] > self.heap[parent]:
            self.__swap(index, parent)
            self.__floatUp(parent)

    def __bubbleDown(self, index):
        left = index * 2
        right = index * 2 + 1
        largest = index
        if len(self.heap) > left and self.heap[largest] < self.heap[left]:
            largest = left
        if len(self.heap) > right and self.heap[largest] < self.heap[right]:
            largest = right
        if largest != index:
            self.__swap(index, largest)
            self.__bubbleDown(largest)

array = [1,-5,3,4,5,6,689584,8,2,2,3,4,72,6,8,7,9,9,10]

m = MaxHeap([])
for i in array :
    m.push(i)

m.heap.pop(0)
print(m.heap)

j = 0
for i in m.heap :
    if j == 0 :
        print(i)
    elif j <= 1 :
        print(i,end=",")
    elif j == 2 :
        print(i)
    elif j <= 5 :
        print(i,end=",")
    elif j == 6 :
        print(i)
    elif j <= 13:
        print(i, end=",")
    elif j == 14 :
        print(i)
    elif j <= 30:
        print(i, end=",")
    j = j + 1

print(m.heap())