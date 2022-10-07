# Old implementation

# def capitalize_all(t):
#     res = []
#     for s in t:
#         res.append(s.capitalize())
#     return res

def capitalize_all(t):
    return [s.capitalize() for s in t]

# Old implementation

# def only_upper(t):
#     res = []
#     for s in t:
#         if s.isupper():
#             res.append(s)
#     return res

def only_upper(t):
    return [s for s in t if s.isupper()]