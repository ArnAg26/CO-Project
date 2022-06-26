def add(e1,e2,e3):
    ans = ""
    ans += dic_isa["add"]["opcode"]
    ans += "00"
    ans += dic_r[e1]
    ans += dic_r[e2]
    ans += dic_r[e3]
    return ans
def sub(e1,e2,e3):
    ans = ""
    ans += dic_isa["sub"]["opcode"]
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
        e2 = str(bin(int(e2[1:])))
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
    ans += dic_isa["ls"]["opcode"]
    ans += dic_r[e1]
    e2 = str(bin(int(e2[1:])))
    if (len(e2) != 8):
        for i in range (0,8-len(e2),1):
            ans += "0"
    ans += e2
    return ans
def ls(e1,e2):
    ans = ""
    ans += dic_isa["ls"]["opcode"]
    ans += dic_r[e1]
    e2 = str(bin(int(e2[1:])))
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
    ans += dic_isa["cmp"]["opcode"]
    ans += "00000"
    ans += dic_r[e1]
    ans += dic_r[e2]
    ans = ""
    return ans
def jmp(e1):
    ans = ""
    ans += dic_isa["jmp"]["opcode"]
    ans += "000"
    r = variable[e1]
    if (len(r) != 8):
        for i in range (0,8-len(r),1):
            ans += "0"
    ans += r
    return ans
def jlt(e1):
    ans = ""
    ans += dic_isa["jmp"]["opcode"]
    ans += "000"
    r = variable[e1]
    if (len(r) != 8):
        for i in range (0,8-len(r),1):
            ans += "0"
    ans += r
    return ans
def jgt(e1):
    ans = ""
    ans += dic_isa["jmp"]["opcode"]
    ans += "000"
    r = variable[e1]
    if (len(r) != 8):
        for i in range (0,8-len(r),1):
            ans += "0"
    ans += r
    return ans
def je(e1):
    ans = ""
    ans += dic_isa["jmp"]["opcode"]
    ans += "000"
    r = variable[e1]
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
}
memory= []
for i in range(0,256,1) :
    memory[i] = str(bin(i))
with open("input.txt","r") as f:
    l = [ x for x in  f.read().split("\n")]
labels = {}
variable = {}
counter = -1
file = open("Output.txt","w")
for i in l:
    counter += 1
    if i == " ":
        pass
    else:
        m = [x for x in l.split()]
        if m[0] == "var" :
            variable[m[1]] = memory[counter]    
        if m[0][-1] == ":" :
            labels[m[0][0:-1]] = memory[counter]
            m = m[1:]
        if m[0] == "add":
            ans = add(m[1],m[2],m[3])
        elif m[0] == "sub":
            ans = sub(m[1],m[2],m[3])
        elif m[0] == "mov":
            t = False
            if m[2][1] == "$":
                t = True
            ans = mov(m[1],m[2],t)
        elif m[0] == "ld":
            ans = ld(m[1],m[2])
        elif m[0] == "st":
            ans = st(m[1],m[2])
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
            ans = je(m[1])
        elif m[0] == "hlt":
            ans = hlt()
    f.write(ans + "\n")
f.close()