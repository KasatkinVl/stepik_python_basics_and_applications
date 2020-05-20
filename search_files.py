import os.path

print(os.getcwd())
os.chdir("C:\\Users\\User\\Downloads\\")
print(os.getcwd())

list_of =[]
for i in os.walk("main"):
    for file in i[2]:
        if file[-3:] == '.py':
            list_of.append(i[0])
            break

with open("C:\\Users\\User\\Downloads\\ans.txt", "w") as ans:
    ans.write("\n".join(sorted(list_of)))

