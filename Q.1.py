# # # shorting the dictionary
# # a={'sanjna':32,'laddu':21,'sadu':33}
# # # a={1:12,2:23,3:34,4:54,5:22,6:1}
# # for i in a:                  
# #   for j in a:
# #     if a[i]<a[j]:
# #       tem=a[i]
# #       a[i]=a[j] 
# #       a[j]=tem
# # print(a)

# a=["nitin","tanu","12321","pavap"]
# i=0
# while i<len(a):
#     j=0
#     b=''
#     c=''
#     while j<len(a[i]):
#         b+=a[i][j]
#         j+=1
#     # print(b)
#     j=1
#     while j<=len(a[i]):
#         c+=a[i][-j]
#         j+=1
#     # print(c)
#     i+=1
#     if b==c:
#         print(b,"palindrome")
#     else:
#         print(b,"not")



# a=[104,501,608]
# #[140,510,680]
# i=0
# b=[]
# while i<len(a):
#     if a[i]==0:
#         pass
#     else:
#         b.append(a[i])
#     i+=1
# i=0
# while i<len(a):
#     if a[i]!=0:
#         pass
#     else:
#         b.append(a[i])
#     i+=1
# print(b)


# a=[2030,708,6008,100,5007]
# i=0
# m=[]
# while i<len(a):
#     a[i]=str(a[i])
#     b=[]
#     j=0
#     while j<len(a[i]):
#         if a[i][j]==0:
#             pass
#         else:
#             b.append(int(a[i][j]))
#         j+=1
#     t=0
#     while t<len(a[i]):
#         if a[i][t]!=0:
#             pass
#         else:
#             b.append(int(a[i][t]))
#         t+=1
#     i+=1
#     m.append(b)
# print(m)





# s='abcd'
# s=s[-1]+s[1:-1]+s[0]
# print(s)

# #dbca

# s="my name is abc"
# a=[]
# t=""
# for i in s:
#     if i=="":
#         a.append(t)
#         t=""
#     else:
#         t+=i
# if t :
#     a.append(t)
#     print(a)



a=[104,5001,601,30405]
#[140,510,680]
i=0
l=[]
while i<len(a):
    a[i]=str(a[i])
    j=0
    b=""
    while j<len(a[i]):
            
        if a[i][j]=='0':
            pass
        else:
            b+=((a[i][j]))
        j+=1
    print(b)
    t=0
    while t<len(a[i]):
        if a[i][t]!='0':
            pass
        else:
            b+=((a[i][t]))
        t+=1
    l.append(int(b))
    i+=1
print(l)


# a="my name is aarti biradar"
# # o/p='my','name','is ','aarti','biradar'
# b=[]
# t=""
# for i in a:
#     if i =="":
#         t=""
#     else:
#         t+=i
# if t :
#     b.append(t)
# print(b)

# a="my name is aarti biradar"
# a1=len(a)-1
# list1=[]
# str=""
# i=0
# while i<=len(a):
#     if a[i]==" ":
#         list1.append(str)
#         str=""
#     elif i==a1:
#         str+=a[i]
#         list1.append(str)
#         break
#     else:
#         str+=a[i]
#     i+=1
# print(list1)

# def rev(a):
    
#     b=[]
#     i=1
#     while i<=a:
#         f=int(input("enter the number "))
#         b.append(f)
#         i+=1
#     print(b)
#     i=1
#     c=[]
#     while i<len(b)+1:
#         c.append(b[-i])
#         i+=1
#     print(c)
# a=int(input("enter the"))
# rev(a)


# def re():
#     b=int(input("enter the number "))
#     a=['a', 1, '2', 5, 'b', 'q']
#     i=1
#     while i<=b:
#         print(a[-i])
#         i+=1
# re()


# def name(b):
#     a=['a', 1, '2', 5, 'b', 'q']
#     i=0
#     while i<=(b)+1:
#         print(a[-b])
#         i+=1
#         b-=1
# b=int(input("enter the number "))
# name(b)




# num=int(input("enter the length:-"))
# i=0
# a=[]
# while i<=num:
#     number=int(input("enter :-"))
#     a.append(number)
#     i+=1
# print(a)
# s=0
# for i in a:
#     print(i)
#     s+=i
# if i%2==0:
#     print("true")
# else:
#     print("not")
# dic={'a':5,'b':10,'a':6,'c':20}
# b={}
# for i in dic:
#     if i not in b:
#         b.update({i:dic[i]})
# print(b)

# a=["ankita","tanu","dimple"]
# b={}
# for i in a:
#     b.update({i:len(i)})
# print(b)

# a={'name':20,'class':4,'RollNo':5}
# b={'name':5,'seussion':5,'RollNo':5}
# s=0
# dic={}
# for i in a:
#     for j in b:
#         if i==j:
#             s=a[i]+b[j]
#             dic.update({i:s})
# dic.update({i:a[i]})
# print(dic)


# d1 = {'a': 100, 'b': 200, 'z':300}
# d2 = {'a': 300, 'b': 200, 'x':400}
# sum=0
# n={}
# for i in d1:
#     for j in d2:
#         if i==j:
#             sum=d1[i]+d2[j]
#             n.update({i:sum}) 
# n.update({i:d1[i]})
# print(n)


# print(s)


# my={'a':27,'b':43,'c':25,'d':30}
# valA=""
# for i in my:
#     if i>valA:
#         valA=i
#         valB=my[i]
# print(valB)

# d={'n':'a','ag':5,'sal':25000}
# val=d['ag']
# if val in d:
#     print("this")
# else:
#     print("this is")