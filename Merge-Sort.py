#Divide and Conquer - Merge Sort Algorithm Practice

def Merge(A, p, q, r):
    n1=q-p+1
    n2=r-q
    L=[]
    R=[]
    for i in range(0, n1):
        L.append(A[p+i])
    for j in range(0, n2):
        R.append(A[q+j+1])
    i=0
    j=0
    for k in range(p, r+1):
        if i+p>q:
            A[k]=R[j]
            j=j+1
        elif j+p>q:
            A[k]=L[i]
            i=i+1
        elif L[i]<=R[j]:
            A[k]=L[i]
            i=i+1
        else:
            A[k]=R[j]
            j=j+1
    return(A)

def MergeSort(A, p, r):
    if p<r:
        q=int(((p+r)/2))
        MergeSort(A, p, q)
        MergeSort(A, q+1, r)
        Merge(A, p, q, r)
    return(A)
            
A=[1,6,10,12,2,5,7,11]

#B=Merge(A, 0, 3, 7)
C=MergeSort(A, 0, len(A)-1)
print(C)
