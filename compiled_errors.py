def haltError(lst):
    if lst[-1]!=['hlt']:
        return 0
    for i in range(len(lst)-1):
            if lst[i]==['hlt']:
                return -1
    return 1

#print(haltError(lst))
def VarList(lst,varlist):    #ins_l,[]
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


def Labellist(lst,labellist):   #ins_l,[]
    i=0
    for i in range(len(lst)):
        # if len(lst[i])>1 and lst[i][1][-1]==":":
        #     return -1
        if lst[i][0][-1]==":":
            labellist.append(lst[i][0][:-1])
    
    return 1
            

def UndefinedVariables(lst,varlist,labellist):  #ins_l, varlist, labellist
    for i in range(len(lst)):
        if lst[i][0] in ["ld","st"]:
            y=lst[i][-1]
            if y not in varlist and y not in labellist:
                return -1
            elif y not in varlist and y in labellist:
                return 0
    return 1
            
            
            
def UndefinedLabels(lst,varlist,labellist):     #ins_l,varlist,labellist
    for i in range(len(lst)):
        if lst[i][0] in ["jmp","jgt","je","jlt"]:
            y=lst[i][-1]
            if y not in labellist and y not in varlist:
                return -1
            elif y not in labellist and y in varlist:
                return 0
    return 1
                
        
def ImmediateError(lst):             #insl_l
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

def IllegalFlag(lst):         #insl_l
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

def ErrorCheck(lst):        #ins_l
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


def is_valid_opcode(ins_l):

    #check if length is correct

    d=[' ','add','sub','mov','ld','st','mul','div','rs','ls',
    'xor','or','and','not','cmp','jmp','jlt','jgt','je','hlt',
    'var']

    for i in ins_l:
        if (i[0][-1]==":"):
            continue;
        
        elif i[0] not in d:
            return -1
    
    return 1


def error_len(ins_l):

    d={'add':3,'sub':3,'mov':3,'ld':3,'st':3,'mul':4,'div':3,'rs':3,'ls':3,'xor':4,'or':4,'and':4,
    'not':3,'cmp':3,'jmp':2,'jlt':2,'jgt':2,'je':2,'hlt':1,'var':2}

    for i in ins_l:
        if (i[0][-1]==":"):
            continue
        if (len(i)!=d[i[0]]):
            # print(i)
            return -1
    
    return 1


def reg_error_l1(l1):

    # is it between R0 and R6
    #the first letter is a R and not a,b,c,d or r

    regl=['R0','R1','R2','R3','R4','R5','R6']

    reg=l1[0]

    if (ord(reg[0])!=82):
        return -1

    elif (reg not in regl):
        return -1

    return 1

def reg_error_l2(l2):

    reg1=l2[0]
    reg2=l2[1]

    regl=['R0','R1','R2','R3','R4','R5','R6']


    if (ord(reg1[0])!=82 or ord(reg2[0]!=82)):
        return -1

    elif (reg1 not in regl) or (reg2 not in regl):
        return -1

    return 1
    

def reg_error_l3(l3):

    reg1=l3[0]
    reg2=l3[1]
    reg3=l3[2]

    regl=['R0','R1','R2','R3','R4','R5','R6']


    fc1=ord(reg1[0])
    fc2=ord(reg2[0])
    fc3=ord(reg3[0])

    if (fc1!=82 or fc2!=82 or fc3!=82):
        return -1
    
    elif (reg1 not in regl) or (reg2 not in regl) or (reg3 not in regl):
        return -1

    return 1

def check_mov(l):

    if (l[-1][0]=='$' and l[0][0]!='$'):
        regl=['R0','R1','R2','R3','R4','R5','R6']

        reg=l[0]
        fc=reg[0]

        if (ord(fc)!=82):
            return -1
        elif (reg not in regl):
            return -1
        
        return 1

    elif (l[0][0]=='$'):
        return -1    

    else:

        regl=['R0','R1','R2','R3','R4','R5','R6']

        reg1=l[0]
        reg2=l[1]

        fc1=reg1[0]
        fc2=reg2[0]

        if (ord(fc1)!=82 or ord(fc2)!=82):
            return -1

        elif (reg1 not in regl) or (reg2 not in regl):
            return -1
        
        return 1





def syntax_error(insl):

    l1=[]
    l2=[]
    l3=[]

    d3=['add','sub','mul','xor','or','and']
    d2=['div','not','cmp']
    d1=['ls','rs','ld','st']

    for i in insl:
        if i[0][-1]==":":
            continue
        if i[0]=='mov':
            a=check_mov(i[1:])
            if (a==-1):
                return -1

        elif i[0] in d1:
            l1.append(i[1:])

        elif i[0] in d2:
            l2.append(i[1:])

        elif i[0] in d3:
            l3.append(i[1:])

    # print(l1)
    # print(l2)
    # print(l3)
    


    for i in l1:
        e1=reg_error_l1(i)

        if(e1==-1):
            return -1

    for i in l2:
        e2=reg_error_l2(i)

        if (e1==-1):
            return -1

    for i in l3:
        e3=reg_error_l3(i)

        if (e3==-1):
            return -1

    return 1
    # e1=reg_error_l1(l1)
    # e2=reg_error_l2(l2)
    # e3=reg_error_l3(l3)

    # if (e1 and e2 and e3):
    #     return 1
    # else:
    #     return -1
    



with open("t.txt",'r') as f:

    ins_l=[]
    for i in f.readlines():
        split=i.split()
        if (split!=[]):
            ins_l.append(i.split())
    
    # print(ins_l)
    if (is_valid_opcode(ins_l)==-1):
        print("Invalid instruction used")

    elif ((error_len(ins_l))==-1 or (syntax_error(ins_l))==-1):
        print("Invalid syntax")

    else:
        print(ErrorCheck(ins_l))
    



    f.close()

