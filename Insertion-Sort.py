#Insertion Sort Algorithm Implementation as part of CLRS Algorithms Practice

def insertionsort(Array):
    #Keep first number same, start comparing with second number in array
    for j in range(1, len(Array)):
        #Make key holder since we will be replacing jth term with j-1 until
        #we get to the point where the jth term needs to be placed
        key=Array[j]
      #  print('Key in round '+str(j)+' is '+str(key))
        i=j-1
        #Starting at the jth number, we go back in the array while making j-1th term
        #with previous terms until it is no longer greater than current term.
        while i>=0 and Array[i]>key:
            Array[i+1]=Array[i]
            #print('Array sorting: '+str(Array))
            i=i-1
        Array[i+1]=key
       # print('Array sorting: '+str(Array))
    return(Array)

#Random consistent number array generator
import random

random.seed(14)
Array=[1]
for x in range(1, 100):
    Array.append(int(100*random.random()))

print(insertionsort(Array))

