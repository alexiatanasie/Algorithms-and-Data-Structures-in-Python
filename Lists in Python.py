#called list in Python, usually this is called an array
#if you want to use an array - then you use NumPy arrays
my_list=[1,4,7,8,9]
print(my_list[1])

my_list=list((1,4,7,8,9))
print(my_list)  #print the list itself

my_list=['my name is ale',13,9]
print(my_list)


for item in my_list:
    print(item)

print(len(my_list))
print(type(my_list))
my_list[0]='my name is steph'
my_list[1] = 22
for item in my_list:
    print(item)


#del operator will remove a given item
del my_list[0]
print(len(my_list))
print(my_list)

#appending a new item at the end of the list is O(1)
my_list.append('this is a new item')
#beacuse listst are indexed , there may be multiple items with the same value
my_list.append('this is the last item')

print(my_list[-1]) #last item of the list
print(my_list[-2])

print(my_list[0:2])

print(25*"-")

list1=[1,"list 1",9.6]
list2=[True,"list2", False]

#concatenate given lists
result=list1+list2
print(result)
#var2
list1.extend(list2)
print(list1)

#the lists's built-in functions
list1.append("new item")
print(list1)

result=list1.copy()
print(result)

list1.remove(9.6)
print(list1)

#this is O(1) because we manipulate the last item
result=list1.pop() #af ultimul item
print(result)

list1.reverse()
print(list1)

list_names=['ale','steph','nick','adele','aylin']
list_names.sort()
print(list_names)

list_=[48,90,2,55,78,12,5]
list_.sort()
print(list_)

#list comprehension :allows as to create a new list based on existing values of another list

numbers=[1,100,6,88,78,76,33,47,89,90,23]

new_list=[]
for num in numbers:
    if num%2==0:
        new_list.append(num)
print(new_list)

new_list=[num for num in numbers if num%2==0] #called list compreh.
print(new_list)

names=['ale','steph','daniel','marlena','anna']
filtered_names=[]
for name in names:
    if name.startswith('a'):
        filtered_names.append(name)
print(filtered_names)


filtered_names=[name for name in names if name.startswith('a')]
print(filtered_names)

#if we want to get the names with 4 letters
filtered_names=[name for name in names if len(name)==5]
print(filtered_names)


