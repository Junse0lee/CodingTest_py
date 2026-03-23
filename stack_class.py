class stack:
    def __init__(self):
        self.items= []

    def push(self, data):
        self.items.append(data)

    def pop(self):
        pop_object = None
        if self.isEmpty():
            print("stack is empty")
        else:
            pop_object = self.items.pop()

        return pop_object
    
    def peak(self):
        if self.isEmpty():
            print("stack is empty")
        else:
            print(self.items[-1])
        
    def isEmpty(self):
        is_empty= False
        if len(self.items) == 0:
            is_empty= True
        return is_empty
    
    def command_empty(self):
        for _ in range(len(self.items)):
            self.pop()
            answer = self.isEmpty()
            if answer == True:
                print("이제부터 이 stack은 비었습니다. 따란~")
                break

    

mystack = stack()
mystack.push(10)
mystack.push(10)
mystack.push(20)
mystack.push(30)

mystack.peak()

removed__data = mystack.pop()
print(f"꺼낸 값: {removed__data}")

answer= mystack.isEmpty()
print(f"이 스택은 비었나요? {answer}")

mystack.command_empty()

