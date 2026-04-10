repeat_num = int(input())
l = list(map(int, input().split()))
max_num = max(l)

for i in range(repeat_num):
    l[i] = l[i]/max_num *100
    

avg_num = sum(l) / repeat_num

print(avg_num)