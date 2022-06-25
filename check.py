
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

    elif (l[0][0]=='$' and l[-1][0]!='$'):
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
   



with open("t.txt",'r') as f:

    ins_l=[]
    for i in f.readlines():
        split=i.split()
        if (split!=[]):
            ins_l.append(i.split())
    
    print(ins_l)
    print(is_valid_opcode(ins_l));
    print(error_len(ins_l))
    print(syntax_error(ins_l))

    



    f.close()

