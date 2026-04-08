l = []
max_values= -1

for i in range(9):
    num = int(input())
    l.append(num)
    
    if num > max_values:
        max_values = num
        max_index = i
        
print(max_values)
print(max_index+1)