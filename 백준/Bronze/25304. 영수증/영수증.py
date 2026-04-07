sum_price = int(input())
repeat = int(input())
predict_price = 0
for i in range(repeat):
    each_price, count = map(int, input().split())
    predict_price += each_price *count
    
if predict_price == sum_price:
    print('Yes')
else:
    print('No')