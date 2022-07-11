# Write a program to sort a dictionary in ascending or descending according 
# to its values .
# Input :-
# Code Example

# {'param':20,'anjili':30,'bijender':45,'roshini':50,'deepak':60}
# Expected result in Descending Order:

# {'deepak':60,'roshini':50,'bijender':45,'anjili':30,'param':20}

a={'bijender':45,'deepak':60,'param':20,'anjili':30,'roshini':50}
l=[]
for i in a:
    l.append(a[i])
    for i in range(len(l)):
        for j in range(len(l)):
            if l[i]<l[j]:
                l[i],l[j]=l[j],l[i]
print(l)
d={}
for h in l:
    for g in a:
        if a[g]==h:
            d.update({g:h})
print(d)
   
# a={'bijender':45,'deepak':60,'param':20,'anjili':30,'roshini':50}
# l=[]
# for i in a:
#     l.append(a[i])
#     for i in range(len(l)):
#         for j in range(len(l)):
#             if l[i]<l[j]:
#                 l[i],l[j]=l[j],l[i]
# # print(l)
# d={}
# for h in l:
#     for g in a:
#         if a[g]==h:
#             d.update({g:h})
# print(d)



# # set ascending
# a={3,2,1,4,5,6}
# for i in a:                  
#   for j in a:
#      if i >j:
#        b=i
#        i=j
#        j=b   
# print((a)) 




