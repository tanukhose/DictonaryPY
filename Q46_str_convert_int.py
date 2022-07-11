# Q46.Write a Python program to convert string values of a given dictionary, into integer/float datatypes. Go to the editor
# Original list:
# [{'x': '10', 'y': '20', 'z': '30'}, {'p': '40', 'q': '50', 'r': '60'}]
# String values of a given dictionary, into integer types:
# [{'x': 10, 'y': 20, 'z': 30}, {'p': 40, 'q': 50, 'r': 60}]
# Original list:
# [{'x': '10.12', 'y': '20.23', 'z': '30'}, {'p': '40.00', 'q': '50.19', 'r': '60.99'}]
# String values of a given dictionary, into float types:
# [{'x': 10.12, 'y': 20.23, 'z': 30.0}, {'p': 40.0, 'q': 50.19, 'r': 60.99}]



a=[{'x': '10', 'y': '20', 'z': '30'}, {'p': '40', 'q': '50', 'r': '60'}]
b=[]
for i in a:
    if i !=list:
        d={}
        # print(i)
        for j in i:
            # print(i[j])
            d[j]=int(i[j])
        b.append(d)
print(b)





a=[{'x': '10.12', 'y': '20.23', 'z': '30'}, {'p': '40.00', 'q': '50.19', 'r': '60.99'}]
b=[]
for i in a:
    if i!=list:
        d={}
        for j in i:
            d.update({j:float(i[j])})
    b.append(d)
print(b)


