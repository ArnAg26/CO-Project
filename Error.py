
def haltError(lst,linelist):
    if lst[-1]!=['hlt']:
        return 0,linelist[-1]
    for i in range(len(lst)-1):
            if lst[i]==['hlt']:
                return -1,linelist[i]
    return 1,0

#print(haltError(lst))
def VarList(lst,varlist,linelist):    #ins_l,[]
    i=0
    while lst[i][0]=='var':
        if len(lst[i])>2:
            return -1,linelist[i]
        varlist.append(lst[i][1])
        i+=1
    j=i
    for i in range(j,len(lst)):
        if lst[i][0]=='var':
            return -1,linelist[i]
    return 1,0


def Labellist(lst,labellist):   #ins_l,[]
    i=0
    for i in range(len(lst)):
        # if len(lst[i])>1 and lst[i][1][-1]==":":
        #     return -1
        if lst[i][0][-1]==":":
            labellist.append(lst[i][0][:-1])
    
    return 1,0
            

def UndefinedVariables(lst,varlist,labellist,linelist):  #ins_l, varlist, labellist
    for i in range(len(lst)):
        if lst[i][0] in ["ld","st"]:
            y=lst[i][-1]
            if y not in varlist and y not in labellist:
                return -1,linelist[i]
            elif y not in varlist and y in labellist:
                return 0,linelist[i]
    return 1,0
            
            
            
def UndefinedLabels(lst,varlist,labellist,linelist):     #ins_l,varlist,labellist
    for i in range(len(lst)):
        if lst[i][0] in ["jmp","jgt","je","jlt"]:
            y=lst[i][-1]
            if y not in labellist and y not in varlist:
                return -1,linelist[i]
            elif y not in labellist and y in varlist:
                return 0,linelist[i]
    return 1,0
                
        
def ImmediateError(lst,linelist):             #insl_l
    for i in range(len(lst)):
        if lst[i][0]=="mov" and lst[i][2][0]=="$":
            if int(lst[i][2][1:])<0 or int(lst[i][2][1:])>255:
                return -1,linelist[i]
        elif lst[i][0] in ["ls","rs"]:
            if lst[i][2][0]!="$":
                return 0,linelist[i]
            elif int(lst[i][2][1:])<0 or int(lst[i][2][1:])>255:
                return -1,linelist[i]
    return 1,0

def IllegalFlag(lst,linelist):         #insl_l
    for i in range(len(lst)):
        if lst[i][0] in ["add","sub","mul","xor","or","and"]:
            if lst[i][1]=="FLAGS" or lst[i][2]=="FLAGS" or lst[i][3]=="FLAGS:":
                return -1,linelist[i]
        elif lst[i][0] in ["cmp","not","div"]:
            if lst[i][1]=="FLAGS" or lst[i][2]=="FLAGS":
                return -1,linelist[i]
        elif lst[i][0] in ["mov","ld","st","rs","ls"]:
            if lst[i][1]=="FLAGS":
                return -1,linelist[i]
    return 1,0



def is_valid_opcode(ins_l,linelist):

    #check if length is correct

    d=[' ','add','sub','mov','ld','st','mul','div','rs','ls',
    'xor','or','and','not','cmp','jmp','jlt','jgt','je','hlt',
    'var']

    for i in range(len(ins_l)):
        if (ins_l[i][0][-1]==":"):
            continue
        elif ins_l[i][0] not in d:
            return -1,linelist[i]
    
    return 1,0


def error_len(ins_l,linelist):

    d={'add':3,'sub':3,'mov':3,'ld':3,'st':3,'mul':4,'div':3,'rs':3,'ls':3,'xor':4,'or':4,'and':4,
    'not':3,'cmp':3,'jmp':2,'jlt':2,'jgt':2,'je':2,'hlt':1,'var':2}

    for i in range(len(ins_l)):
        if (ins_l[i][0][-1]==":"):
            continue
        if (len(ins_l[i])!=d[ins_l[i][0]]):
            # print(i)
            return -1,linelist[i]
    
    return 1,0


def reg_error_l1(l1):

    # is it between R0 and R6
    #the first letter is a R and not a,b,c,d or r

    regl=['R0','R1','R2','R3','R4','R5','R6','FLAGS']

    reg=l1[1]


    if (reg not in regl):
        return -1

    return 1

def reg_error_l2(l2):

    reg1=l2[1]
    reg2=l2[2]

    regl=['R0','R1','R2','R3','R4','R5','R6','FLAGS']
    if (reg1 not in regl) or (reg2 not in regl):
        return -1

    return 1
    

def reg_error_l3(l3):

    reg1=l3[1]
    reg2=l3[2]
    reg3=l3[3]

    regl=['R0','R1','R2','R3','R4','R5','R6','FLAGS']
    
    if (reg1 not in regl) or (reg2 not in regl) or (reg3 not in regl):
        return -1

    return 1

def check_mov(l,linelist):

    if (l[-1][0]=='$' and l[0][0]!='$'):
        regl=['R0','R1','R2','R3','R4','R5','R6','FLAGS']

        reg=l[0]
        fc=reg[0]
        if (reg not in regl):
            return -1
        
        return 1

    elif (l[0][0]=='$'):
        return -1    

    else:

        regl=['R0','R1','R2','R3','R4','R5','R6','FLAGS']

        reg1=l[0]
        reg2=l[1]

        fc1=reg1[0]
        fc2=reg2[0]
        if (reg1 not in regl) or (reg2 not in regl):
            return -1
        
        return 1

def syntax_error(ins_l,linelist):

    l1=[]
    l2=[]
    l3=[]

    d3=['add','sub','mul','xor','or','and']
    d2=['div','not','cmp']
    d1=['ls','rs','ld','st']

    for i in range(len(ins_l)):
        if ins_l[i][0][-1]==":":
            continue
        if ins_l[i][0]=='mov':
            a=check_mov(ins_l[i][1:],linelist)
            if (a==-1):
                return -1,linelist[i]

        elif ins_l[i][0] in d1:
            l1.append(ins_l[i])

        elif ins_l[i][0] in d2:
            l2.append(ins_l[i])

        elif ins_l[i][0] in d3:
            l3.append(ins_l[i])

    # print(l1)
    # print(l2)
    # print(l3)
    


    for i in range(len(ins_l)):
        if ins_l[i] in l1:
            e1=reg_error_l1(ins_l[i])
            if(e1==-1):
                return -1,linelist[i]

        if ins_l[i] in l2:
            e2=reg_error_l2(ins_l[i])

            if (e1==-1):
                return -1,linelist[i]

        if ins_l[i] in l3:
            e3=reg_error_l3(ins_l[i])

            if (e3==-1):
                return -1,linelist[i]

    return 1,0
    # e1=reg_error_l1(l1)
    # e2=reg_error_l2(l2)
    # e3=reg_error_l3(l3)

    # if (e1 and e2 and e3):
    #     return 1
    # else:
    #     return -1
    
def ErrorCheck(lst,linelist):        #ins_l
    varlist=[]
    labellist=[]
    z,y=is_valid_opcode(lst,linelist)
    if z==-1:
        return "Line "+y+" Invalid instruction used"
    z,y=error_len(lst,linelist)
    if z==-1:
        return "Line "+y+" Invalid syntax"
    z,y=syntax_error(lst,linelist)
    if z==-1:
        return "Line "+y+" Invalid Snytax"
    z,y=VarList(lst,varlist,linelist)
    if z==1:
        pass
        #print(varlist)
    else:
        return "Line "+y+" Variables not defined at start"
    z,y=Labellist(lst,labellist)
    if z==1:
        pass
        #print(labellist)
    else:
        return "Line "+y+" Space between label and colon"
    z,y=ImmediateError(lst,linelist)
    if z==0:
        return "Line "+y+" $ does not preceed immediate value"
    if z==-1:
        return "Line "+y+" Immediate given out of range"
    z,y=UndefinedVariables(lst,varlist,labellist,linelist)
    if z==-1:
        return "Line "+y+" Undefined Variable"
    if z==0:
        return "Line "+y+" Misuse of label as variable"
    z,y=UndefinedLabels(lst,varlist,labellist,linelist)
    if z==-1:
        return "Line "+y+" Undefined Label"
    if z==0:
        return "Line "+y+" Misuse of variable as label"
    z,y=haltError(lst,linelist)
    if z==-1:
        return "Line "+y+" Halt used before last instruction"
    if z==0:
        return "Line "+y+" Halt not used to terminate program"
    z,y=IllegalFlag(lst,linelist)
    if z==-1:
        return "Line "+y+" Illegal usage of flag"
    return "No Errors"
def input():
    with open("input.txt",'r') as f:

        ins_l=[]
        linelist=[]
        ctr=1
        for i in f.readlines():
            split=i.split()
            if (split!=[]):
                if split[0][-1]==":":
                    linelist.append(str(ctr))
                    ins_l.append([split[0]])
                    linelist.append(str(ctr))
                    ins_l.append(split[1:])
                else:
                    linelist.append(str(ctr))
                    ins_l.append(split)
            ctr+=1
        
        #print(ins_l)
        #print(linelist)
        
        x = (ErrorCheck(ins_l,linelist))
        print (x)
        if x ==  "No Errors":
            return 1
        else:
            return 0