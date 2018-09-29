N = int(input())
X = [int(i) for i in input().strip().split(' ')]
W = [int(i) for i in input().strip().split(' ')]
s=0
for i in range(N):
    s = s + X[i]*W[i]
print('{0:.1f}'.format(s/sum(W)))