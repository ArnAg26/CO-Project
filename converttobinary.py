def typea():
    return 
def typeb():
    return
def typec():
    return
def typed():
    return
def typee():
    return
def typef():
    return 
    
ro = 0
r1 = 0
r2 = 0
r3 = 0
r4 = 0
r5 = 0
r6 = 0
flags = 0
v = 0 # overflow
l = 0 # less than
g = 0 # more than
e = 0 # equal than
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
with open("input.txt","r") as f:
    l = [ x for x in  f.read().split("\n")]
labels = {}
for i in l:
    if i == " ":
        pass
    m = [x for x in l.split()]
    if m[0][-1] == ":" :
        labels[m[0:-1]] = 
        m = m[1:]
