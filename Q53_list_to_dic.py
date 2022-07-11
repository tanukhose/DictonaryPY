# Q53.
# Write a Python program to convert a given list of lists to a dictionary. 
# Original list of lists:
# [[1, 'Jean Castro', 'V'], [2, 'Lula Powell', 'V'], [3, 'Brian Howell', 'VI'], [4, 'Lynne Foster', 'VI'], [5, 'Zachary Simon', 'VII']]
# Convert the said list of lists to a dictionary:
# {1: ['Jean Castro', 'V'], 2: ['Lula Powell', 'V'], 3: ['Brian Howell', 'VI'], 4: ['Lynne Foster', 'VI'], 5: ['Zachary Simon', 'VII']}

a=[[1, 'Jean Castro', 'V'], [2, 'Lula Powell', 'V'], 
    [3, 'Brian Howell', 'VI'], [4, 'Lynne Foster', 'VI'], 
    [5, 'Zachary Simon', 'VII']]
b={}
for i in a:
    b.update({i[0]:[i[1],i[2]]})
print(b)