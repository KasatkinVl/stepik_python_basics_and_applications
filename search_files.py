import os
import os.path

print(os.getcwd())
os.chdir("C:\\Users\\User\\Downloads\\")
print(os.getcwd())

list_of =[]
for i in os.walk("."):
    for file in i[2]:
        if file[-3:] == '.py':
            list_of.append(i[0][2:])
            break

l = sorted(list_of)


with open("C:\\Users\\User\\Downloads\\ans.txt", "w") as ans:
    qwe = "\n".join(l)
    ans.write(qwe)

