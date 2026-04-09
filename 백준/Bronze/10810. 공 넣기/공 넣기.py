N, M = map(int, input().split())
l = [0] * N

for _ in range(M):
    I, J, K= map(int, input().split())
    for o in range(I-1, J):
        l[o] = K
        
for x in range(N):
    print(l[x], end= " ")