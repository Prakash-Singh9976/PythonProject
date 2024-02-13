# tup1=("Haddop","Python","Java")
#
# print(len(tup1))
# print(max(tup1))# based on ascending descending
# print(min(tup1))

# tup2 = (1,3,5,2)
# print(sorted(tup2))
# print(tup2[::-1])

# tup = ([0,1,2],[1,2,3],[2,3,4])
# tup[0][1] = 'Updated'
# print(tup)

tuple1 = (1,3,5,7,'a','b')
lst = list(tuple1)# conversion of touple into list using list keyword
print(lst)
lst[1] = 'Python'
print(lst)
tuple2 = tuple(lst)# conversion of list into tuple using tuple keyword
print(tuple2)