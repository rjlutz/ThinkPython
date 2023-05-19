# def delete_head(t):
#     del t[0]
#
# Here’s how it is used:
# >>> letters = ['a', 'b', 'c']
# >>> delete_head(letters)
# >>> letters
# ['b', 'c']

def delete_head(t):
    del t[0]


letters = ['a', 'b', 'c']
delete_head(letters)
print(letters)
