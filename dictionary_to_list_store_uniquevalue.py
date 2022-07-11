a=[
    {'one':'1',
    'scound':'2',
    'thid':'1',
    'four':'5',
    'five':'5',
    'six':'9',
    'seven':'7'
    }
]

# res=set()           #list(set(val for dic))
# for k in a:
#     for val in k.values():
#         res.add(val)
# print(list(res))

b=set()
for k in a:
    for v in k.values():
        b.add(v)
print(list(b))