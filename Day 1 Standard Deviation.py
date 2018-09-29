import math

N = int(input())
X = [int(i) for i in input().strip().split(' ')]

mn = sum(X)/N

s = 0
for i in range(N):
    s = s + ((X[i]-mn)**2)
        
print('{0:.1f}'.format(math.sqrt(s/N)))