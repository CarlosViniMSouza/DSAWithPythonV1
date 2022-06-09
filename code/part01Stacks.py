stack = [3, 4, 5]

stack.append(6)  # added 6
stack.append(7)  # added 7

print(stack)
# output: [3, 4, 5, 6, 7]

print(stack.pop())  # remember: this method removed the last element on list!
# output: 7

print(stack)
# output: [3, 4, 5, 6]

stack.pop()  # dropped 6
stack.pop()  # dropped 5

print(stack)
# output: [3, 4]
