class heap:
    def __init__(self, heap):
        self.length=heap
        self.heapSize=len(heap)
    def parent(self, i):
        return (i+1)/2-1
    def left(self, i):
        return 2*(i+1)-1
    def right(self, i):
        return 2*(i+1)+1-1

def maxHeapify(A, i):
    l=A.left(i)
    r=A.right(i)
    heap=A.length
    if l<A.heapSize and heap[l]>heap[i]:
        largest=l
    else:
        largest=i
    try:
        if r< A.heapSize and heap[r]>heap[largest]:
            largest=r
    except:
        pass
    if largest != i:
        placeholder=heap[i]
        heap[i]=heap[largest]
        heap[largest]=placeholder
        A.length=heap
        maxHeapify(A, largest)
    return A

def minHeapify(A, i):
    l=A.left(i)
    r=A.right(i)
    heap=A.length
    if l<A.heapSize and heap[l]<heap[i]:
        smallest=l
    else:
        smallest=i
    if r<A.heapSize:
        if r< A.heapSize and heap[r]<heap[smallest]:
            smallest=r
    if smallest != i:
        placeholder=heap[i]
        heap[i]=heap[smallest]
        heap[smallest]=placeholder
        A.length=heap
        minHeapify(A, smallest)
    return A

def buildMaxHeap(A):
    for i in range(int(round(A.heapSize/2,0))-1, -1, -1):
        A=maxHeapify(A, i)
    return A

def buildMinHeap(A):
    for i in range(int(round(A.heapSize/2,0))-1, -1, -1):
        A=minHeapify(A, i)
    return A

def heapSort(A):
    A=buildMaxHeap(A)
    for i in range(A.heapSize-1, 0, -1):
        placeholder=A.length[i]
        A.length[i]=A.length[0]
        A.length[0]=placeholder
        A.heapSize=A.heapSize-1
        maxHeapify(A, 0)
    return A

def heapMaximum(A):
    return A[0]

def heapExtractMax(A):
    if A.heapSize<1:
        return "error: heap underflow"
    max=A[0]
    A[0]=A[A.heapSize-1]
    A.heapSize=A.heapSize-1
    A=maxHeapify(A, 0)
    return max

def heapIncreaseKey(A, i, key):
    if key<A.length[i]:
        return "ERROR: new key is smaller than current key"
    A.length[i]=key
    while i>1 and A.length[int(A.parent(i))]<A.length[int(i)]:
        placeholder=A.length[int(A.parent(i))]
        A.length[int(A.parent(i))]=A.length[int(i)]
        A.length[int(i)]=placeholder
        i=A.parent(i)
    return A

def maxHeapInsert(A, key):
    A.heapSize=A.heapSize+1
    print(A.heapSize)
    A.length.append(-99999999)
    A=heapIncreaseKey(A, A.heapSize-1, key)
    return A

A=heap([60, 80,5,65,7, 60, 80, 50])
A=buildMaxHeap(A)
print(A.length)
A=maxHeapInsert(A, 70)
print(A.length)
