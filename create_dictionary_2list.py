

list1=['one','two','three','four','five']
list2=[1,2,3,4,5]
dic={}
for i in list1:
    for j in list2:
        dic[i]=j
        break
print(str(dic))



list1=['one','two','three','four','five']
list2=[1,2,3,4,5]
d={}
for i in range(len(list1)):
    # d.update({list1[i]:list2[i]})
    d[list1[i]]=list2[i]
print(d)    




# remove the duplicate keys:

# dic={
#     'ball':'red',
#     'bat':4,
#     'wickets':8,
#     'ball':'green',
#     'bat':3
#     }
# print(dic)


# a={}
# for i in range(5):
#     key=input("enter the key")
#     value=input("enter the value")
#     a.update({key:value})
# print(a)    


# a=int(input("enter the len"))
# new={}
# for i in range(a):
#     k=input("enter the name")
#     v=int(input("enter the value"))
#     # new[k]=v
#     new.update({k:v})
# print(new)


