stack = []

for i in range(0,10):
    stack.append(i)

print("지금 스택의 크기는")
print(len(stack))

print("스택에서 뺄 때에는")
stack.pop()
print("pop을 이용하면 됩니다!")
print(len(stack))

stack.pop()
stack.pop()


for i in range(0, 3):
    print(stack[-1])
    stack.pop()

    