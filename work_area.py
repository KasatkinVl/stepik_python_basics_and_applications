scopes = {'global': {'parent': None, 'variables': set()}}

def create(nmsp,parent):
    scopes[nmsp] = {'parent': parent, 'variables': set()}

def add(nmsp, arg):
    scopes[nmsp]['variables'].add(arg)

def get(nmsp, arg):
    for key_parent in scopes[nmsp]['parent']:
        if arg in scopes[nmsp]['variables']:
            return scopes[nmsp]

# add global a
# create foo global
# add foo b
# get foo a
# get foo c

n = int(input())

for i in range(n):
    cmmd, nmsp, arg = input().split()

    if cmmd == 'create':
        create(nmsp, arg)

    elif cmmd == 'add':
        add(nmsp, arg)

    elif cmmd == 'get':
        print(get(nmsp, arg))


print(scopes)
