l = []

for i in range(10):
    input_number = int(input())
    value = input_number % 42
    if value not in l:
        l.append(value)
        
print(len(l))