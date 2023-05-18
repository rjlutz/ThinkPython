# def only_upper(t):
#     res = []
#     for s in t:
#         if s.isupper():
#             res.append(s)
#     return res

def only_upper(t):
    res = []
    for s in t:
        if s.isupper():
            res.append(s)
    return res


inp = ['go lions!', 'Go Lions!', 'GO LIONS!']
uppers = only_upper(inp)
print(f'input: {inp}')
print(f'uppers: {uppers}')
