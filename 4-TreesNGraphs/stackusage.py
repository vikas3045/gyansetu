from collections import deque
""" Stack usage """
stack = []
print(stack)

stack.append(1)
print(stack)

stack.append(2)
print(stack)

stack.append(3)
print(stack)

print(stack.pop())
print(stack)

# for peek
print(stack[-1])


""" Queue usage """


queue = deque([1, 2, 3, 4])
print(queue)

queue.append(5)
print(queue)

queue.append(6)
print(queue)

print(queue.popleft())
print(queue)

#for peek
print(queue[0])
