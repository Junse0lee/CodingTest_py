N, M = map(int, input().split())
bucket = []
#init
for x in range(N):
    bucket.append(x+1)

for i in range(M):
    num1, num2 = map(int, input().split())
    temp = bucket[num1-1]
    bucket[num1-1] = bucket[num2 -1]
    bucket[num2-1] = temp
    
for p in range(N):
    print(bucket[p])