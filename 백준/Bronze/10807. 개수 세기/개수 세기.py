num = int(input())
l = list(map(int, input().split()))
find_num = int(input())

count = 0 
for i in range(num):
    if find_num == l[i]:
        count +=1

print(count)