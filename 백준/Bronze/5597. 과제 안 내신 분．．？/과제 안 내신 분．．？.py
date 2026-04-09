total_student = 30
none_student = []
for i in range(28):
    none_student.append(int(input()))
    
for i in range(1, 31):
    if i not in none_student:
        print(i)
