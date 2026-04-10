N, M= map(int, input().split())
l=[]
for num in range(N):
    l.append(num+1)

for p in range(M):
    i, j = map(int, input().split())
    i-=1
    j -=1
    while i<j:
        l[i], l[j]= l[j], l[i]
        i+=1
        j-=1

print(*l)