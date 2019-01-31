#Radix sort sample

def radixSort(A, d):
    #going through each column in the number, we sort the column starting at the
    #ones place
    for i in range(1, d+1):
        place=d-i
        for j in range(0, len(A)):
            #Sort each column from the right to the left
            if j==0:
                j=0
            else:
                if int(A[j][place])<int(A[j-1][place]):
                    #If the column in j is greater than the column in j-1
                    #we need to switch them, and then recursively check again
                    #until it has been switched where it needs to go
                    rearrange(A, j, place)
        print(A)
    return(A)

def rearrange(A, j, place):
    #This switches j with j-1
    temp=A[j-1]
    A[j-1]=A[j]
    A[j]=temp
    if j==1:
        return(A)
    else:
        #This checks to see if j-1 is still less than j-2
        #If so, we keep pushing it down until we are in order up to place j
        if int(A[j-1][place])<int(A[j-2][place]):
            A=rearrange(A, j-1, place)
    return(A)

A=['329','457','657','839','436','720','355']

print(radixSort(A, 3))
