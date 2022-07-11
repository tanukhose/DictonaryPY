dict1={
    'alex':['sub1','sub2','sub3'],
    'david':['sub1','sub2']
    }
count=0
for i in dict1:
    if type(dict1[i])==list:
        for j in dict1[i]:
            count+=1
            print(j)
print(count)


