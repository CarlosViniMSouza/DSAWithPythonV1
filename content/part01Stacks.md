## 5.1.1. Using Lists as Stacks

The list methods make it very easy to use a list as a stack, where the last element added is the first element retrieved (“last-in, first-out”). To add an item to the top of the stack, use `append()`. To retrieve an item from the top of the stack, use `pop()` without an explicit index. For example:

```python
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

```
