# ake input of name and marks of 10 students and store to a dictionary.
# Output :-
# Code Example

# {
#  'sonu':85,
#  'Kartik':90,
#  'Deepak':96,
#  'Aman':76,
#  'Somesh':60,
#  'Umesh':85,
#  'Amarpal':70,
#  'Roshan':57,
#  'Riyaz':98,
#  'Shabid':56
# }

person={
    'name':'jack',
    'id':22,
    'place':'pune'
}
person.popitem()
print(person)

# del:-

person={
    'name':'jack',
    'id':22,
    'place':'pune'
}
del person['place']
print(person)


a=int(input("enter the lenght"))
dic={}
for i in range(a):
    name=input("enter the name")
    marks=int(input("enter the marks"))
    # dic.update({name:marks})
    dic[name]=marks
print(dic)

