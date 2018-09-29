N = int(input())
X = [int(i) for i in input().strip().split(' ')]
F = [int(i) for i in input().strip().split(' ')]

def creat_S(X,F):
    S=[]
    for j,f in enumerate(F):
        for i in range(f):
            S.append(X[j])
    S.sort()
    return S
S = creat_S(X,F)

def med(S):
    m = len(S)
    if m%2 == 1:
        med = S[int(m/2)]
    else:
        med = (S[int(m/2)] + S[int(m/2)-1])/2
    return med
    
def quart(S):
    m = len(S)
    if m%2 == 1:
        Q1 = S[:int(m/2)]
        Q2 = S[int(m/2)+1:]
    else:
        Q1 = S[:int(m/2)]
        Q2 = S[int(m/2):]
    q1 = float(med(Q1))
    q2 = float(med(Q2))
    return round((q2 - q1),1)

print(quart(S))
