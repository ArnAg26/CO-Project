#common file for qs 2
def Execution_unit(string,pc):
    opcode = string[0:5]
    if opcode == "10000":    #1
        r1 = string[7:10]
        r2 = string[10:13]
        r3 = string[13:]
        add(r1,r2,r3,pc)
    elif opcode == "10001":   #2
        r1 = string[7:10]
        r2 = string[10:13]
        r3 = string[13:]
        sub(r1,r2,r3,pc)
    elif opcode == "10010":    #3
        r1 = string[5:8]
        imm = string[8:]
        movim(r1,imm,pc)
    elif opcode == "10011":         #4
        r1 = string[10:13]
        r2 = string[13:]
        movre(r1,r2,pc)
    elif opcode == "10100":       #5
        r1 = string[5:8]
        mem_add = string[8:]
        ld(r1,mem_add,pc)
    elif opcode == "10101":      #6
        r1 = string[5:8]
        mem_add = string[8:]
        store(r1,mem_add,pc)
    elif opcode == "10110":       #7
        r1 = string[7:10]
        r2 = string[10:13]
        r3 = string[13:]
        mul(r1,r2,r3,pc)
    elif opcode == "10111":       #8
        r1 = string[10:13]
        r2 = string[13:]
        div(r1,r2,pc)
    elif opcode == "11000":        #9
        r1 = string[5:8]
        imm = string[8:]
        rs(r1,imm,pc) 
    elif opcode == "11001":        #10
        r1 = string[5:8]
        imm = string[8:]
        ls(r1,imm,pc)
    elif opcode == "11010":           #11
        r1 = string[7:10]
        r2 = string[10:13]
        r3 = string[13:]
        XOR(r1,r2,r3,pc)
    elif opcode == "11011":           #12
        r1 = string[7:10]
        r2 = string[10:13]
        r3 = string[13:]
        OR(r1,r2,r3,pc)
    elif opcode == "11100":           #13
        r1 = string[7:10]
        r2 = string[10:13]
        r3 = string[13:]
        AND(r1,r2,r3,pc)
    elif opcode == "11101":           #14
        r1 = string[10:13]
        r2 = string[13:]
        NOT(r1,r2,pc)
    elif opcode == "11110":           #15
        r1 = string[10:13]
        r2 = string[13:]
        CMP(r1,r2,pc)
    elif opcode == "11111":           #16
        mem_add = string[8:]
        JMP(mem_add,pc)
    elif opcode == "01100":           #17
        mem_add = string[8:]
        JLT(mem_add,pc)
    elif opcode == "01101":           #18
        mem_add = string[8:]
        JGT(mem_add,pc)
    elif opcode == "01111":           #19
        mem_add = string[8:]
        JE(mem_add,pc)
    elif opcode == "01010":          #20
        pc = 256
    return pc