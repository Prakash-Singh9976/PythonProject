# list = ["Haddoop","Python","Android"]

# print(list[1])
# print(list[0:2])
# print(list[-1]) # negative takes last element in the list
# print(list[-2])
# print(list[-3])

# print(list + ["React","Angular","data science"])

# print(list*3)

# print('Haddoop' in list,'Angular' in list) # in is used for membership testing

# del(list[2])
# print(list)
# list2 = [1,2,3,4,5,'a','b','c']
# print(list2.pop(3))
# print(list2.remove('a'))
# print(list2)

# list = []
# for x in [1,2,3,4,5]:
#     list.append(x**2) // for single element
# print(list)
# list3 = [x**2 for x in [1,2,3,4,5]]
# print(list3)

# list = [1,2,3]
# list.extend(['g','h'])  # add an item to end of list
# # print(list)
# list.append('Machine learning') #for single element
# # print(list)
# list.insert(2,'Scripting')
# print(list)
# list4= ['Haddoop','Python','Android','Java']
# # print(type(list))
# print(sorted(list4))
# print(list4[::-1])# reverese the list
list5= [(1,2,3),("Python","Java")]
print(list5)
print(len(list5))#calculate length
print(list5[1][0][0:3])#slicing