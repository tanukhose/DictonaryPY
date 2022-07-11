# Q50.Write a Python program to convert a given dictionary into a list of lists. 
# Original Dictionary:
# {1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}
# Convert the said dictionary into a list of lists:
# [[1, 'red'], [2, 'green'], [3, 'black'], [4, 'white'], [5, 'black']]
# Original Dictionary:
# {'1': 'Austin Little', '2': 'Natasha Howard', '3': 'Alfred Mullins', '4': 'Jamie Rowe'}
# Convert the said dictionary into a list of lists:
# [['1', 'Austin Little'], ['2', 'Natasha Howard'], ['3', 'Alfred Mullins'], ['4', 'Jamie Rowe']]


a={1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}
k=[]
for i in a:
    b=[]
    b.append(i)
    b.append(a[i])
    k.append(b)
print(k)




a={'1': 'Austin Little', '2': 'Natasha Howard', '3': 'Alfred Mullins', '4': 'Jamie Rowe'}
list=[]
for i in a:
    l=[]
    l.append(i)
    l.append(a[i])
    list.append(l)
print(list)