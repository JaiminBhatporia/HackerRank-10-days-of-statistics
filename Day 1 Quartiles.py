N = int(input())
X = [int(i) for i in input().strip().split(' ')]
X.sort()

def med(X):
    m = len(X)
    if m%2 == 0:
        result = int((X[int(m/2)] + X[int(m/2) - 1])/2)
    else:
        result = int(X[int(m/2)])
    print(result)

def quart(X):
    m = len(X)
    if m%2 == 0:
        q1 = X[:int(m/2)]
        q2 = X[int(m/2):]
    else:
        q1 = X[:int(m/2)]
        q2 = X[int(m/2)+1:]
    med(q1)
    med(X)
    med(q2)
   
quart(X)