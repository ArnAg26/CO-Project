#common file for qs 2
import sys
from pip import main

def toBinary(deci):

    st=""
    for i in range(16):
        st=st+str(deci%2)
        deci=deci//2
    
    return st[::-1]


        

def toDecimal(imm):

    #101  len=3  1*2^(3-1)+0*2^(3-1-1).....
    wt=len(imm);  #wt=3
    sum=0
    for i in imm:
        sum+=int(i)*2**(wt-1)
        wt-=1

    return sum


def ls(reg, imm,pc):


    imm_in_deci=toDecimal(imm)

    ls=reg_dic[reg]<<imm_in_deci

    reg_dic[reg]=ls%(2**16)

    pc+=1

    return pc


def rs(reg, imm ,pc):

   

    imm_in_deci=toDecimal(imm)

    rs=reg_dic[reg]>>imm_in_deci

    reg_dic[reg]=rs%(2**16)

    pc+=1

    return pc

def jmp(mem_add,pc):
    pc=toDecimal(mem_add)
    return pc
    
def jlt(mem_add,pc):
    if reg_dic['111'][13]=='1':
        pc=toDecimal(mem_add)
        return pc
    return pc+1

def jgt(mem_add,pc):
    if reg_dic['111'][14]=='1':
        pc=toDecimal(mem_add)
        return pc
    return pc+1

def je(mem_add,pc):
    if reg_dic['111'][15]=='1':
        pc=toDecimal(mem_add)
        return pc
    return pc+1



def AND(r1,r2,r3,pc):

    #r1&r2=r3
    reg_dic[r3]=(reg_dic[r1]&reg_dic[r2])%(2**16)

    pc+=1

    return pc


def OR(r1,r2,r3,pc):


    

    reg_dic[r3]=(reg_dic[r1]|reg_dic[r2])%(2**16)

    pc+=1

    return pc


def XOR(r1,r2,r3,pc):

    

    reg_dic[r3]=(reg_dic[r1]^reg_dic[r2])%(2**16)

    pc+=1

    return pc




def NOT(r1,r2,pc):

    

    reg_dic[r2]=(~reg_dic[r1])%(2**16)

    pc+=1

    return pc

def ld(r1,mem_add,pc):
    a=toDecimal(mem[toDecimal(mem_add)])
    reg_dic[r1]=a
    pc+=1
    variable_dic[toDecimal(mem_add)]=a
    return pc

    
    
def store(r1,mem_add,pc):
    a=toBinary(reg_dic[r1])
    mem[toDecimal(mem_add)]=a
    pc+=1
    return pc
    
    

def add(r1,r2,r3,pc):
    q = reg_dic[r1]
    r = reg_dic[r2]
    p = reg_dic[r3]
    p = q + r
    if p > 2**16 -1:
        reg_dic["111"][-4] = '1'
        reg_dic[r3] = p % (2**16)
    else:
        reg_dic[r3] = p
    pc += 1
    return pc

def sub(r1,r2,r3,pc):
    p = reg_dic[r1]
    q = reg_dic[r2]
    r = reg_dic[r3]
    r = p - q
    if r < 0:
        reg_dic["111"][-4] = '1'
        reg_dic[r3] = 0
    else:
        reg_dic[r3] = r
    pc += 1
    return pc

def mul(r1,r2,r3,pc):
    q = reg_dic[r1]
    p = reg_dic[r2]
    r = reg_dic[r3]
    r = q * p
    if r > 2**16 -1:
        reg_dic["111"][-4] = '1'
        reg_dic[r3] = r % (2**16)
    else:
        reg_dic[r3] = r
    pc += 1
    return pc

def div(r1,r2,pc):
    p = reg_dic[r1]
    q = reg_dic[r2]
    if q != 0:
        quo = int(p/q)
        rem = p - quo*q
        reg_dic["000"] = quo
        reg_dic["001"] = rem
    pc += 1
    return pc

def movim(r1,imm,pc):
    ans = toDecimal(imm)
    reg_dic[r1] = ans
    pc += 1
    return pc
    
def movre(r1,r2,pc):
    if r1 == "111":
        ans = toBinary(reg_dic[r2])
        reg_dic["111"][-4:] = ans[-4:]
    else:
        reg_dic[r2] = reg_dic[r1]
    pc += 1
    return pc

def CMP(r1,r2,pc):
    p = reg_dic[r1]
    q = reg_dic[r2]
    if (p>q):
        reg_dic["111"][-2] = '1'
    elif (p<q):
        reg_dic["111"][-3] = '1'
    else:
        reg_dic["111"][-1] = '1'
    pc += 1
    return pc


def Execution_unit(string,pc):
    opcode = string[0:5]
    if opcode == "10000":    #1
        r1 = string[7:10]
        r2 = string[10:13]
        r3 = string[13:]
        pc = add(r1,r2,r3,pc)
    elif opcode == "10001":   #2
        r1 = string[7:10]
        r2 = string[10:13]
        r3 = string[13:]
        pc = sub(r1,r2,r3,pc)
    elif opcode == "10010":    #3
        r1 = string[5:8]
        imm = string[8:]
        pc = movim(r1,imm,pc)
    elif opcode == "10011":         #4
        r1 = string[10:13]
        r2 = string[13:]
        pc = movre(r1,r2,pc)
    elif opcode == "10100":       #5
        r1 = string[5:8]
        mem_add = string[8:]
        pc = ld(r1,mem_add,pc)
    elif opcode == "10101":      #6
        r1 = string[5:8]
        mem_add = string[8:]
        pc = store(r1,mem_add,pc)
    elif opcode == "10110":       #7
        r1 = string[7:10]
        r2 = string[10:13]
        r3 = string[13:]
        pc = mul(r1,r2,r3,pc)
    elif opcode == "10111":       #8
        r1 = string[10:13]
        r2 = string[13:]
        pc = div(r1,r2,pc)
    elif opcode == "11000":        #9
        r1 = string[5:8]
        imm = string[8:]
        pc = rs(r1,imm,pc) 
    elif opcode == "11001":        #10
        r1 = string[5:8]
        imm = string[8:]
        pc = ls(r1,imm,pc)
    elif opcode == "11010":           #11
        r1 = string[7:10]
        r2 = string[10:13]
        r3 = string[13:]
        pc = XOR(r1,r2,r3,pc)
    elif opcode == "11011":           #12
        r1 = string[7:10]
        r2 = string[10:13]
        r3 = string[13:]
        pc = OR(r1,r2,r3,pc)
    elif opcode == "11100":           #13
        r1 = string[7:10]
        r2 = string[10:13]
        r3 = string[13:]
        pc = AND(r1,r2,r3,pc)
    elif opcode == "11101":           #14
        r1 = string[10:13]
        r2 = string[13:]
        pc = NOT(r1,r2,pc)
    elif opcode == "11110":           #15
        r1 = string[10:13]
        r2 = string[13:]
        pc = CMP(r1,r2,pc)
    elif opcode == "11111":           #16
        mem_add = string[8:]
        pc = jmp(mem_add,pc)
    elif opcode == "01100":           #17
        mem_add = string[8:]
        pc = jlt(mem_add,pc)
    elif opcode == "01101":           #18
        mem_add = string[8:]
        pc = jgt(mem_add,pc)
    elif opcode == "01111":           #19
        mem_add = string[8:]
        pc = je(mem_add,pc)
    elif opcode == "01010":          #20
        pc = 256
    return pc

l=sys.stdin.readlines()
mem=[]
for i in l:
    if i=='\n':
        continue
    mem.append(i.strip("\n"))
n=len(mem)

for i in range(n,256):
    mem.append('0000000000000000')





reg_dic={'000':0,'001':0,'010':0,'011':0,'100':0,'101':0,'110':0,'111':'0000000000000000'}
label_dic = {}
variable_dic = {}
if __name__== "__main__":

    pc=0

    while (1):
        ans = toBinary(pc)
        ans = ans[8:]
        print(ans,end=" ")

        pc=Execution_unit(mem[pc],pc)

        print(toBinary(reg_dic['000']),end=" ")
        print(toBinary(reg_dic['001']),end=" ")
        print(toBinary(reg_dic['010']),end=" ")
        print(toBinary(reg_dic['011']),end=" ")
        print(toBinary(reg_dic['100']),end=" ")
        print(toBinary(reg_dic['101']),end=" ")
        print(toBinary(reg_dic['110']),end=" ")
        print(toBinary(reg_dic['111']),end=" ")
        print("\n")


        if pc==256:
            break
    for i in mem:
        print(i)