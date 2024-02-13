# x = set('Welcome to edureka')
# print(x)
#
# A = {1,2,2,3,4}
# B = {5,6,7,4,3}
# print(A|B) #union operator
# print(A&B)#intersection operator
# print(A-B)#value inside a which are not in b

s = {1,2,3,'a','b'}
set1 = {1,'a','b'}

# print(1 in s)
#
# print(set1.issubset(s))
#
# print(5 not in s)
#
# print(s.issuperset(set1))
#
# print(s.union(set1))
#
# print(s.intersection(set1))
#
# print(s.difference(set1))
#
# print(s.symmetric_difference(set1))

# s.add('h')
# print(s)
# s.remove(65)#throws an error if element is not present
# print(s)
# s.discard(16)#it will not throws an error if element is not present
# print(s)

s.pop()# remove first element
print(s)
s.clear()#remove all element from set
print(s)