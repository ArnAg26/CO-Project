import sys

def floatingbinary(m):
    ans = bin(int(m))[2:]
    p1 = m - (int (m))
    n = len(str(p1)) - 2
    p = int(p1 * (2**n))
    lm = bin(p)[2:]
    len_lm = n - len(lm)
    ans += "."
    for i in range(0,len_lm):
        ans += "0"
    for i in lm:
        ans += i
    return (ans)

def isvalid_float(m):
    ans = floatingbinary(ans)
    if len(ans) > 7:
        return 0
    return 1

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

def Labellist(lst,labellist,linelist,extra):   #ins_l,[]
    i=0
    for i in range(len(extra)):

        ctr=[x for x in extra[i] if x[-1]==':']
        if len(ctr)>1:
            return -1,linelist[i]
    # print(extra)
    for i in range(len(lst)):
        # print(labellist)
        # if len(lst[i])>1 and lst[i][1][-1]==":":
        #     return -1
        if lst[i][0][-1]==":":
            if lst[i][0][:-1] in labellist:
                return -1,linelist[i]
            else:
                labellist.append(lst[i][0][:-1])
    # for i in range(len(extra)):
    #     if extra[i]
    
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
            if "." in lst[i][2][1:]:
                return -2,linelist[i]
            elif int(lst[i][2][1:])<0 or int(lst[i][2][1:])>255:
                return -1,linelist[i]
        elif lst[i][0] == "movf" and lst[i][2][0]=="$":
            if "." not in lst[i][2][1:]:
                return -3,linelist[i]
            elif ~isvalid_float(lst[i][2][1:]):
                return -1,linelist[i]            
        elif lst[i][0] in ["ls","rs"]:
            if lst[i][2][0]!="$":
                return 0,linelist[i]
            elif "." in lst[i][2][1:]:
                return -2,linelist[i]
            elif int(lst[i][2][1:])<0 or int(lst[i][2][1:])>255:
                return -1,linelist[i]
    return 1,0

def IllegalFlag(lst,linelist):
    for i in range(len(lst)):
        if lst[i][0] in ["add","sub","mul","xor","or","and"]:
            # print(lst[i])
            if lst[i][1]=="FLAGS" or lst[i][2]=="FLAGS" or lst[i][3]=="FLAGS":
                # print(lst[i][0])
                return -1,linelist[i]
        elif lst[i][0] in ["cmp","not","div"]:
            if lst[i][1]=="FLAGS" or lst[i][2]=="FLAGS":
                return -1,linelist[i]
        elif lst[i][0] in ["ld","st","rs","ls"]:
            if lst[i][1]=="FLAGS":
                return -1,linelist[i]
        elif lst[i][0] in ["mov"]:
            if lst[i][2]=="FLAGS" or (lst[i][2][0]=="$" and lst[i][1]=="FLAGS"):
                return -1,linelist[i]
    return 1,0

def is_valid_opcode(ins_l,linelist):

    #check if length is correct

    d=[' ','add','sub','mov','ld','st','mul','div','rs','ls',
    'xor','or','and','not','cmp','jmp','jlt','jgt','je','hlt',
    'var','movf','addf','subf']
    # print(ins_l)
    for i in range(len(ins_l)):

        if (ins_l[i][0][-1]==":"):
            continue
        elif ins_l[i][0] not in d:
            return -1,linelist[i]
    
    return 1,0

def error_len(ins_l,linelist):

    d={'add':4,'sub':4,'mov':3,'ld':3,'st':3,'mul':4,'div':3,'rs':3,'ls':3,'xor':4,'or':4,'and':4,
    'not':3,'cmp':3,'jmp':2,'jlt':2,'jgt':2,'je':2,'hlt':1,'var':2,'movf': 3,'addf':4,'subf':4}

    for i in range(len(ins_l)):
        
        if (ins_l[i][0][-1]==":"):
            continue
        elif (len(ins_l[i])!=d[ins_l[i][0]]):
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

    d3=['add','sub','mul','xor','or','and','addf','subf']
    d2=['div','not','cmp']
    d1=['ls','rs','ld','st']

    for i in range(len(ins_l)):
        
        

        if ins_l[i][0][-1]==":":
            continue
        elif ins_l[i][0]=='mov' :
            a=check_mov(ins_l[i][1:],linelist)
            if (a==-1):
                return -1,linelist[i]
        elif ins_l[i][0] == 'movf':
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

            if (e2==-1):
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
    
def ErrorCheck(lst,linelist,extra):        #ins_l
    varlist=[]
    labellist=[]
    # print(lst)
    z,y=haltError(lst,linelist)
    if z==-1:
        return "Line "+y+" Halt used before last instruction"
    if z==0:
        return "Line "+y+" Halt not used to terminate program"
    z,y=VarList(lst,varlist,linelist)
    if z==1:
        pass
        #print(varlist)
        
    else:
        return "Line "+y+" Variables not defined at start"
    z,y=Labellist(lst,labellist,linelist,extra)
    if z==1:
        # print(labellist)
        pass
    elif (z==-1):
        return "Line "+y+" Invalid use of labels"

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
    z,y=IllegalFlag(lst,linelist)
    if z==-1:
        return "Line "+y+" Illegal usage of flag"
    
    z,y=ImmediateError(lst,linelist)
    if z==0:
        return "Line "+y+" $ does not preceed immediate value"
    if z==-1:
        return "Line "+y+" Immediate given out of range"
    if z==-2:
        return "Line "+y+" Immediate cannot be floating point number"
    if z == -3:
        return "Line "+y+" Immediate cannot be int number"
    z,y=is_valid_opcode(lst,linelist)
    if z==-1:
        return "Line "+y+" Invalid instruction used"
    z,y=error_len(lst,linelist)
    if z==-1:
        return "Line "+y+" Invalid syntax"
    z,y=syntax_error(lst,linelist)
    if z==-1:
        return "Line "+y+" Invalid Syntax"
    return "No Errors"
def input(L):
    ctr=1
        # print(f.readlines())
    for i in L:
            split=i.split()
            extra.append(i.split())
            #print(split)
            
            if (split!=[]):
                if split[0][-1]==":":
                    linelist.append(str(ctr))
                    ins_l.append([split[0]])
                    if (len(split)>1):

                        linelist.append(str(ctr))
                        ins_l.append(split[1:])
                else:
                    linelist.append(str(ctr))
                    ins_l.append(split)
            ctr+=1
    # print(ins_l)
    #print(linelist)
    if len(ins_l)==0:
        print("Line",len(L),"Halt Instruction missing")
        return 0
    #print(linelist)
    x = (ErrorCheck(ins_l,linelist,extra))
            
    if x ==  "No Errors":
                return 1
    else:
        print (x)
        return 0
    
def addf(e1,e2,e3):
    ans = ""
    ans += dic_isa["add"]["opcode"]
    ans += "00"
    ans += dic_r[e1]
    ans += dic_r[e2]
    ans += dic_r[e3]
    return ans

def subf(e1,e2,e3):
    ans = ""
    ans += dic_isa["add"]["opcode"]
    ans += "00"
    ans += dic_r[e1]
    ans += dic_r[e2]
    ans += dic_r[e3]
    return ans

def movf(e1,e2):
    ans = ""
    ans +=  dic_isa["movf"]["opcode"]
    ans +=  dic_r[e1]
    e2 = floatingbinary(float(e2[1:]))
    n = len(e2) - e2.index(".") - 1
    ans += bin(n)[2:]
    for i in e2[1:]:
        if i == ".":
            pass
        else:
            ans += i
    return ans
        
def add(e1,e2,e3):
    ans = ""
    ans += dic_isa["addf"]["opcode"]
    ans += "00"
    ans += dic_r[e1]
    ans += dic_r[e2]
    ans += dic_r[e3]
    return ans
def sub(e1,e2,e3):
    ans = ""
    ans += dic_isa["subf"]["opcode"]
    ans += "00"
    ans += dic_r[e1]
    ans += dic_r[e2]
    ans += dic_r[e3]
    return ans
def mov(e1,e2,e3):
    ans = ""
    if e3:
        ans +=  dic_isa["mov1"]["opcode"]
        ans +=  dic_r[e1]
        e2 = str(bin(int(e2[1:])))[2:]
        if (len(e2) != 8):
            for i in range (0,8-len(e2),1):
                ans += "0"
        ans += e2
    else:
        ans +=  dic_isa["mov2"]["opcode"]
        ans += "00000"
        ans +=  dic_r[e1]
        ans +=  dic_r[e2]
    return ans
def ld(e1,e2):
    ans = ""
    ans += dic_isa["ld"]["opcode"]
    ans += dic_r[e1]
    r = variable[e2]
    if (len(r) != 8):
        for i in range (0,8-len(r),1):
            ans += "0"
    ans += r
    return ans
def st(e1,e2):
    ans = ""
    ans += dic_isa["st"]["opcode"]
    ans += dic_r[e1]
    r = variable[e2]
    if (len(r) != 8):
        for i in range (0,8-len(r),1):
            ans += "0"
    ans += r
    return ans
def mul(e1,e2,e3):
    ans = ""
    ans += dic_isa["mul"]["opcode"]
    ans += "00"
    ans += dic_r[e1]
    ans += dic_r[e2]
    ans += dic_r[e3]
    return ans
def div(e1,e2):
    ans = ""
    ans += dic_isa["div"]["opcode"]
    ans += "00000"
    ans += dic_r[e1]
    ans += dic_r[e2]
    return ans
def rs(e1,e2):
    ans = ""
    ans += dic_isa["rs"]["opcode"]
    ans += dic_r[e1]
    e2 = str(bin(int(e2[1:])))[2:]
    if (len(e2) != 8):
        for i in range (0,8-len(e2),1):
            ans += "0"
    ans += e2
    return ans
def ls(e1,e2):
    ans = ""
    ans += dic_isa["ls"]["opcode"]
    ans += dic_r[e1]
    e2 = str(bin(int(e2[1:])))[2:]
    if (len(e2) != 8):
        for i in range (0,8-len(e2),1):
            ans += "0"
    ans += e2
    return ans
def xor(e1,e2,e3):
    ans = ""
    ans += dic_isa["xor"]["opcode"]
    ans += "00"
    ans += dic_r[e1]
    ans += dic_r[e2]
    ans += dic_r[e3]
    return ans
def or1(e1,e2,e3):
    ans = ""
    ans += dic_isa["or"]["opcode"]
    ans += "00"
    ans += dic_r[e1]
    ans += dic_r[e2]
    ans += dic_r[e3]
    return ans
def and1(e1,e2,e3):
    ans = ""
    ans += dic_isa["and"]["opcode"]
    ans += "00"
    ans += dic_r[e1]
    ans += dic_r[e2]
    ans += dic_r[e3]
    return ans
def not1(e1,e2):
    ans = ""
    ans += dic_isa["not"]["opcode"]
    ans += "00000"
    ans += dic_r[e1]
    ans += dic_r[e2]
    return ans
def cmp(e1,e2):
    ans = ""
    ans += dic_isa["cmp"]["opcode"]
    ans += "00000"
    ans += dic_r[e1]
    ans += dic_r[e2]
    return ans
def jmp(e1):
    ans = ""
    ans += dic_isa["jmp"]["opcode"]
    ans += "000"
    r = labels[e1]
    if (len(r) != 8):
        for i in range (0,8-len(r),1):
            ans += "0"
    ans += r
    return ans
def jlt(e1):
    ans = ""
    ans += dic_isa["jlt"]["opcode"]
    ans += "000"
    r = labels[e1]
    if (len(r) != 8):
        for i in range (0,8-len(r),1):
            ans += "0"
    ans += r
    return ans
def jgt(e1):
    ans = ""
    ans += dic_isa["jgt"]["opcode"]
    ans += "000"
    r = labels[e1]
    if (len(r) != 8):
        for i in range (0,8-len(r),1):
            ans += "0"
    ans += r
    return ans
def je(e1):
    # print(e1)
    ans = ""
    ans += dic_isa["je"]["opcode"]
    ans += "000"
    r = labels[e1]
    if (len(r) != 8):
        for i in range (0,8-len(r),1):
            ans += "0"
    ans += r
    return ans
def hlt():
    ans = ""
    ans += dic_isa["hlt"]["opcode"]
    ans += "00000000000"
    return ans

l=sys.stdin.readlines()


ins_l = []
linelist=[]
extra=[]
y =  input(l)
if y :
    dic_r = {"R0" : "000","R1" : "001", "R2" : "010" , "R3" : "011" , "R4" : "100" , "R5" : "101" , "R6" :"110", "FLAGS" : "111"}
    dic_isa = {
        "add" : {"opcode" : "10000", "type" : "a"},
        "sub" : {"opcode" : "10001", "type" : "a"},
        "mov1" : {"opcode" : "10010", "type" : "b"},
        "mov2" : {"opcode" : "10011", "type" : "c"},
        "ld" : {"opcode" : "10100", "type" : "d"},
        "st" : {"opcode" : "10101", "type" : "d"},
        "mul" : {"opcode" : "10110", "type" : "a"},
        "div" : {"opcode" : "10111", "type" : "c"},
        "rs" : {"opcode" : "11000", "type" : "b"},
        "ls" : {"opcode" : "11001", "type" : "b"},
        "xor" : {"opcode" : "11010", "type" : "a"},
        "or" : {"opcode" : "11011", "type" : "a"},
        "and" : {"opcode" : "11100", "type" : "a"},
        "not" : {"opcode" : "11101", "type" : "c"},
        "cmp" : {"opcode" : "11110", "type" : "c"},
        "jmp" : {"opcode" : "11111", "type" : "e"},
        "jlt" : {"opcode" : "01100", "type" : "e"},
        "jgt" : {"opcode" : "01101", "type" : "e"},
        "je" : {"opcode" : "01111", "type" : "e"},
        "hlt" : {"opcode" : "01010", "type" : "f"},
        "movf" : {"opcode" : "00010", "type" : "b"},
        "addf" : {"opcode" : "00000", "type" : "a"},
        "subf" : {"opcode" : "00001", "type" : "a"},
    }
    memory= []
    for i in range(0,256,1) :
        x = str(bin(i))[2:]
        memory.append(x)
    # print(ins_l)
    labels = {}
    variable = {}
    counter = 0
    num_var = 0
    empty = 0
    for i in l:
        if i != "\n":
            m = [x for x in i.split()]
            if m[0][-1] == ":":
                m = m[1:]
            if m != []:
                if m[0] == "var":
                    num_var += 1
            else:
                empty += 1
        else:
            empty += 1
    length = len(l) - num_var -empty
    for i in l:
        # print(counter,"\n")
        if i == "\n":
            # counter -= 1
            # print(counter,"\n")
            pass
        else:
            m = [x for x in i.split()]
            # print(i.split())
            # print(m)
            if m[0] == "var" :
                variable[m[1]] = memory[counter + length]   
            if m[0][-1] == ":" :
                # print(m)
                labels[m[0][0:-1]] = memory[counter - num_var]
                # print(m[0][0:-1])
                m = m[1:]
            if m != []:
                counter += 1
    for i in l:
        flag = 1
        ans = ""
        if i == "\n":
            flag = 0
            pass
        else:
            m = [x for x in i.split()]
            if m[0] == "var":
                flag = 0
                pass
            if m[0][-1] == ":" :
                m = m[1:]
            if m == []:
                flag = 0
                pass
            elif m[0] == "add":
                ans = add(m[1],m[2],m[3])
            elif m[0] == "sub":
                ans = sub(m[1],m[2],m[3])
            elif m[0] == "mov":
                t = False
                if m[2][0] == "$":
                    t = True
                ans = mov(m[1],m[2],t)
            elif m[0] == "ld":
                ans = ld(m[1],m[2])
            elif m[0] == "st":
                ans = st(m[1],m[2])
                #f.write("f")
            elif m[0] == "mul":
                ans = mul(m[1],m[2],m[3])
            elif m[0] == "div":
                ans = div(m[1],m[2])
            elif m[0] == "rs":
                ans = rs(m[1],m[2])
            elif m[0] == "ls":
                ans = ls(m[1],m[2])
            elif m[0] == "xor":
                ans = xor(m[1],m[2],m[3])
            elif m[0] == "or":
                ans = or1(m[1],m[2],m[3])
            elif m[0] == "and":
                ans = and1(m[1],m[2],m[3])
            elif m[0] == "not":
                ans = not1(m[1],m[2])
            elif m[0] == "cmp":
                ans = cmp(m[1],m[2])
            elif m[0] == "jmp":
                ans = jmp(m[1])
            elif m[0] == "jlt":
                ans = jlt(m[1])
            elif m[0] == "jgt":
                ans = jgt(m[1])
            elif m[0] == "je":
                # print (labels.keys())
                ans = je(m[1])
            elif m[0] == "hlt":
                ans = hlt()
            elif m[0] == "movf":
                ans = movf(m[1],m[2])
            elif m[0] == "addf":
                ans = addf(m[1],m[2],m[3])
            elif m[0] == "subf":
                ans = subf(m[1],m[2],m[3])
        if flag == 1:
            print(ans)