# Q48.Write a Python program to find the length of a given dictionary values. 
# Original Dictionary:
# {1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}
# Length of dictionary values:
# {'red': 3, 'green': 5, 'black': 5, 'white': 5}
# Original Dictionary:
# {'1': 'Austin Little', '2': 'Natasha Howard', '3': 'Alfred Mullins', '4': 'Jamie Rowe'}
# Length of dictionary values:
# {'Austin Little': 13, 'Natasha Howard': 14, 'Alfred Mullins': 14, 'Jamie Rowe': 10}



# a={1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}
# b={}
# for i in a.values():
#     c=0
#     for j in i:
#         c+=1
#         b.update({i:c})
# print(b)


a={'1': 'Austin Little', '2': 'Natasha Howard', '3': 'Alfred Mullins', '4': 'Jamie Rowe'}
b={}
for i in a:
    c=0
    for j in a[i]:
        c+=1
        b.update({a[i]:c})
print(b)
