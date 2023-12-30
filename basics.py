"""
first programming in python
"""
print(type(True))
first_name = "eddie"
last_name= " woo"
print("my first name is {} and last name is {}:" .format(first_name, last_name))

my_str = "Aadarsha Thapa Magar"
print(my_str.find('g'))
add = list()
add=['name', ' age', 'address', ' qualitfication']
print(type(add))
print(add[:-1])

my_str = "alpha"
print(my_str.endswith('a'))

#list
list_exam = ['vision', 'pro', 'apple', 23]
print(len(list_exam))
print(type(list_exam))
print(list_exam[0][4:6])

"""
a ds in python that is mutable and changable
"""
add.append('projects') # adding in last of list
#print(add.append('work experience'))
add.append("internship")
print(add)

lst = list()
lst = [1,2,3,4,5,6]
lst.extend([8,9])
print(lst)
print(sum(lst))
lst.append(sum)
print(lst)
lst.pop(3)
print(lst.index(6))