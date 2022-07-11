# Write a program to print the top 3 highest values of a given dictionary.
# Example :-
# Code Example
#  Output :-

# expect result:-['e','b','c']


my_dict = {
    'a':50, 
    'b':58,
    'c': 56,
    'd':40,
    'e':100, 
    'f':20
    }
h1=0
h2=0
h3=0
for i in my_dict:
    if my_dict[i]>h1:
        h1=my_dict[i]
        k1=i
for i in my_dict:
    if my_dict[i]>h2 and my_dict[i]!=h1:
        h2=my_dict[i]
        k2=i
for i in my_dict:
    if my_dict[i]>h3 and my_dict[i]!=h1 and my_dict[i]!=h2:
        h3=my_dict[i]
        k3=i
print([k1,k2,k3])
