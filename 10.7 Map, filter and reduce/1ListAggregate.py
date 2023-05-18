# def add_all(t):
#     total = 0
#     for x in t:
#         total += x
#     return total

#  run in the debugger, observing each comment!
def add_all(t):
    total = 0  # total is initialized to 0
    for x in t:  # Each time through the loop, x gets one element from the list
        total += x  # The += operator provides a short way to update a variable.
    return total


t = [1, 2, 3, 4]
result = add_all(t)
print(result)
