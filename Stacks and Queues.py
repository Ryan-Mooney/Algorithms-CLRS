class S:
    def __init__(self, array, n):
        self.top=len(array)-1
        self.max=n-1
        temp=array
        for i in range(len(array), n):
            temp.append(0)
        self.self=temp
            

def stackEmpty(S):
    if S.top==-1:
        return True
    else:
        return False

def push(S, x):
    if S.max==S.top:
        return "error overflow"
    S.top=S.top+1
    S.self[S.top]=x

def pop(S):
    if stackEmpty(S):
        return "error underflow"
    else:
        temp=S.self[S.top]
        S.self[S.top]=0
        S.top=S.top-1
    return temp

Stack=S([1,2,3], 10)

class Q:
    def __init__(self, array, n):
        self.head=0
        self.tail=len(array)
        self.length=n
        temp=array
        for i in range(len(array), n):
            temp.append(0)
        self.self=temp

def enqueue(Q, x):
    if Q.head==Q.tail and Q.self[Q.head]!=0:
        return "error full queue"
    Q.self[Q.tail]=x
    if Q.tail==Q.length:
        Q.tail=0
    else:
        Q.tail=Q.tail+1

def dequeue(Q):
    if Q.head==Q.tail and Q.self[Q.head]==0:
        return "error empty queue"
    x=Q.self[Q.head]
    Q.self[Q.head]=0
    if Q.head==Q.length:
        Q.head=0
    else:
        Q.head=Q.head+1
    return x

Queue=Q([1,2,3], 10)
