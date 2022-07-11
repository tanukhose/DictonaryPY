# Q51.Write a Python program to filter even numbers from a given dictionary values. 
# Original Dictionary:
# {'V': [1, 4, 6, 10], 'VI': [1, 4, 12], 'VII': [1, 3, 8]}
# Filter even numbers from said dictionary values:
# {'V': [4, 6, 10], 'VI': [4, 12], 'VII': [8]}
# Original Dictionary:
# {'V': [1, 3, 5], 'VI': [1, 5], 'VII': [2, 7, 9]}
# Filter even numbers from said dictionary values:
# {'V': [], 'VI': [], 'VII': [2]}



# a={'V': [1, 4, 6, 10], 'VI': [1, 4, 12], 'VII': [1, 3, 8]}
# b={}
# for i in a:
#     # print(i)
#     l=[]
#     for j in a[i]:
#         # print(j)
#         if j%2==0:
#             l.append(j)
        
#     b.update({i:l})
# print(b)




a={'V': [1, 3, 5], 'VI': [1, 5], 'VII': [2, 7, 9]}
b={}
for i in a:
    l=[]
    for j in a[i]:
        if j%2==0:
            l.append(j)
    b.update({i:l})
print(b)