class array:
    def __init__(self, array):
        self.array=array
        self.arraySize=len(array)
    def parent(self, i):
        return (i+1)/2-1
    def left(self, i):
        return 2*(i+1)-1
    def right(self, i):
        return 2*(i+1)+1-1

def countingSort(A, B, k):
    C=[]
    for i in range(0, k+1):
        C.append(0)
    for j in range(0, A.arraySize):
        C[A.array[j]]=C[A.array[j]]+1
    for i in range(0, k+1):
        if i==0:
            C[i]=C[i]
        else:
            C[i]=C[i]+C[i-1]
    for j in range(A.arraySize-1, -1, -1):
        B.array[C[A.array[j]]-1]=A.array[j]
        C[A.array[j]]=C[A.array[j]]-1
    return B.array
    

A=array([2,5,3,0,2,3,0,3])
C=array([2,5,3,0,2,3,0,3])
B=countingSort(A, C, 5)
print(B)
