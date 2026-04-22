stack = []

def push(value):
    stack.append(value)
    return stack

def pop():
    if len(stack) > 0:
        stack.pop()
    else:
        print('Stack is empty')
    return stack

push(10)
push(20)
push(30)

print('After push:',stack)
pop()
print('After pop:',stack)

