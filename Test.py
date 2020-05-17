parent_namespace = {'global':'None'}
namespace_vars = {'global':[]}
flag = ''

def create(nmsp,parent):
    parent_namespace[nmsp] = parent
    namespace_vars[nmsp] = []

def add(nmsp, arg):
    namespace_vars[nmsp].append(arg)

def get(nmsp, arg):


    if nmsp in namespace_vars.keys():
        if arg in namespace_vars[nmsp]:
            return nmsp
        else:
            for parents in parent_namespace:
                if parent_namespace[parents] == nmsp:
                    flag = parents
                    if flag == 'None':
                        return 'None'
            return get(flag, arg)


# 9
# add global a
# create foo global
# add foo b
# get foo a
# get foo c
# create bar foo
# add bar a
# get bar a
# get bar b

n = int(input())

for i in range(n):
    cmmd, nmsp, arg = input().split()

    if cmmd == 'create':
        create(nmsp, arg)

    elif cmmd == 'add':
        add(nmsp, arg)

    elif cmmd == 'get':
        print(get(nmsp, arg))

