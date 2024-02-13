import os
newfile = open("Edureka_Py.txt","r")
# newfile.close()
# for i in range(0,10):
#     newfile.write("\n Hello , welcome to Python:");

# print(newfile.mode)
# print(newfile.name)
# print(newfile.softspace)

for i in range(0, 10):
    print(newfile.read())

# os.rename("Edureka_Py.txt","new.txt")
# os.remove("new.txt")

print(newfile.tell())