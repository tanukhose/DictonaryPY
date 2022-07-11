# What will be the output of the following code snippet?
# Code Example

a = {(1,2):1,(2,3):2}
print(a[1,2])

# # Options :-

# B. 1

a = {'a':1,'b':2,'c':3}

# print(a['a','b'])

# Options :-

# A. Key Error


fruit={}
def addone(index):
    if index in fruit:
        fruit [index] += 1
    else:
        fruit[index] = 1
addone('Apple')
addone('Banana')
addone('apple')
addone('Apple')

print(len(fruit))
print(fruit)












# Question 4

# What will be the output of the following code snippet?
# Code Example

Student = {}
Age = {}
Details = {}
Student['name'] = "bikki"
Age['student_age'] = 14
Details['Student'] = Student
Details['Age'] = Age

print(len(Details["Student"])) 





# Question 5

# What will be the output of the following code snippet?
# Code Example

my_dict = {}
my_dict[(1,2,4)] = 8
my_dict[(4,2,1)] = 10
my_dict[(1,2)] = 12

sum = 0
for k in my_dict:
    sum += my_dict[k]
    print(my_dict[k])

print(sum)
print(my_dict)
