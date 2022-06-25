with open("input4.txt","r") as f:
    L=f.readlines()
    lst=[]
    for i in L:
        i=i.split()
        if i!=[]:
            lst.append(i)

def printInput(lst):
    for i in lst:
        print(i)
        
        
printInput(lst)

def haltError(lst):
    if lst[-1]!=['hlt']:
        return 0
    for i in range(len(lst)-1):
            if lst[i]==['hlt']:
                return -1
    return 1

#print(haltError(lst))
def VarList(lst,varlist):
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


def Labellist(lst,labellist):
    i=0
    for i in range(len(lst)):
        if len(lst[i])>1 and lst[i][1][-1]==":":
            return -1
        elif lst[i][0][-1]==":":
            labellist.append(lst[i][0][:-1])
            return 1
            

def UndefinedVariables(lst,varlist,labellist):
    for i in range(len(lst)):
        if lst[i][0] in ["ld","st"]:
            y=lst[i][-1]
            if y not in varlist and y not in labellist:
                return -1
            elif y not in varlist and y in labellist:
                return 0
    return 1
            
            
            
def UndefinedLabels(lst,varlist,labellist):
    for i in range(len(lst)):
        if lst[i][0] in ["jmp","jgt","je","jlt"]:
            y=lst[i][-1]
            if y not in labellist and y not in varlist:
                return -1
            elif y not in labellist and y in varlist:
                return 0
    return 1
                
        
def ImmediateError(lst):
    for i in range(len(lst)):
        if lst[i][0]=="mov" and lst[i][2][0]=="$":
            if int(lst[i][2][1:])<0 or int(lst[i][2][1:])>255:
                return -1
        elif lst[i][0] in ["ls","rs"]:
            if lst[i][2][0]!="$":
                return 0
            elif int(lst[i][2][1:])<0 or int(lst[i][2][1:])>255:
                return -1
    return 1

def IllegalFlag(lst):
    for i in range(len(lst)):
        if lst[i][0] in ["add","sub","mul","xor","or","and"]:
            if lst[i][1]=="FLAGS" or lst[i][2]=="FLAGS" or lst[i][3]=="FLAGS:":
                return -1
        elif lst[i][0] in ["cmp","not","div"]:
            if lst[i][1]=="FLAGS" or lst[i][2]=="FLAGS":
                return -1
        elif lst[i][0] in ["mov","ld","st","rs","ls"]:
            if lst[i][1]=="FLAGS":
                return -1
    return 1

def ErrorCheck(lst):
    varlist=[]
    labellist=[]
    if VarList(lst,varlist)==1:
        print(varlist)
    else:
        return "Variables not defined at start"
    if Labellist(lst,labellist)==1:
        print(labellist)
    else:
        return "Space between label and colon"
    z=ImmediateError(lst)
    if z==0:
        return "$ does not preceed immediate value"
    if z==-1:
        return "Immediate given out of range"
    z=UndefinedVariables(lst,varlist,labellist)
    if z==-1:
        return "Undefined Variable"
    if z==0:
        return "Misuse of label as variable"
    z=UndefinedLabels(lst,varlist,labellist)
    if z==-1:
        return "Undefined Label"
    if z==0:
        return "Misuse of variable as label"
    z=haltError(lst)
    if z==-1:
        return "Halt used before last instruction"
    if z==0:
        return "Halt not used to terminate program"
    if IllegalFlag(lst)==-1:
        return "Illegal usage of flag"
    return "No Errors"

print(ErrorCheck(lst))

            
            



            
        
        
        
        
    
