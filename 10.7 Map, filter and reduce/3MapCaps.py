# def capitalize_all(t):
#     res = []
#     for s in t:
#         res.append(s.capitalize())
#     return res

def capitalize_all(t):
    res = []
    for s in t:
        res.append(s.capitalize())
    return res


inp = ['go lions!', 'Go Lions!', 'GO LIONS!']
capped = capitalize_all(inp)
print(f'input: {inp}')
print(f'capped: {capped}')
