# Q52. Write a Python program to find the specified number of maximum values in a given dictionary.
# Original Dictionary:
# {'a': 5, 'b': 14, 'c': 32, 'd': 35, 'e': 24, 'f': 100, 'g': 57, 'h': 8, 'i': 100}
# 1 maximum value(s) in the said dictionary:
# ['f']
# 2 maximum value(s) in the said dictionary:
# ['f', 'i']
# 5 maximum value(s) in the said dictionary:
# ['f', 'i', 'g', 'd', 'c']


# a={'a': 5, 'b': 14, 'c': 32, 'd': 35, 'e': 24, 'f': 200, 'g': 57, 'h': 8, 'i': 100}
# max1=0
# max2=0
# max3=0
# max4=0
# max5=0
# for i in a:
#     if a[i]>max1:
#         max1=a[i]
#         k=i
# for i in a:
#     if a[i]>max2 and a[i]!=max1:
#         max2=a[i]
#         k2=i
# for i in a:
#     if a[i]>max3 and a[i]!=max2 and a[i]!=max1:
#         max3=a[i]
#         k3=i
# for i in a:
#     if a[i]>max4 and a[i]!=max3 and a[i]!=max2 and a[i]!=max1:
#         max4=a[i]
#         k4=i
# for i in a:
#     if a[i]>max5 and a[i]!=max4 and a[i]!=max3 and a[i]!=max2 and a[i]!=max1:
#         max5=a[i]
#         k5=i
# print([k,k2,k3,k4,k5])
# print(max1)
# print(max2)
# print(max3)
# print(max4)
# print(max5)



a={'a': 5, 'b': 14, 'c': 32, 'd': 35, 'e': 24, 'f': 200, 'g': 57, 'h': 8, 'i': 100}
l=[]
for i in a:
    l.append(a[i])
    for i in range(len(l)):
        for j in range(len(l)):
            if l[i]>l[j]:
                l[i],l[j]=l[j],l[i]
print(l)
k=[]
for n in range(0,5):
    for m in a:
        if l[n]==a[m]:
            k.append(m)
print(k)