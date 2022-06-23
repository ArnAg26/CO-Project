with open("input4.txt","r") as f:
    L=f.readlines()
    lst=[]
    for i in L:
        lst.append(i.split())

def printInput(lst):
    for i in lst:
        print(i)
        
        
printInput(lst)

def haltError(lst):
    if lst[-1]!=['hlt']:
        return -1
    for i in range(len(lst)-1):
            if lst[i]==['hlt']:
                return -1
    return 1

#print(haltError(lst))
varlist=[]
def VarList(lst):
    i=0
    while lst[i][0]=='var':
        if len(lst[i])>2:
            return -1
        varlist.append(lst[i][1])
        i+=1
    j=i
    for i in range(j,len(lst)):
        if lst[i][0]=='var':
            return -1
    return 1

def UndefinedVariables(lst,varlist):
    for i in range(len(lst)):
        if lst[i][0] in ["ld","st"]:
            y=lst[i][-1]
            if y not in varlist:
                return -1
            else:
                return 1
        

if VarList(lst)==1:
    print(varlist)
else:
    print(VarList(lst))
    
print(UndefinedVariables(lst,varlist))

            
        
        
        
        
    