from email.headerregistry import Address
from math import *

print("------------------4 Types of Memory------------------")
print("1. Bit Addressable Memory - Cell Size = 1 bit")
print("2. Nibble Addressable Memory - Cell Size = 4 bit")
print("3. Byte Addressable Memory - Cell Size = 8 bits(standard)")
print("4. Word Addressable Memory - Cell Size = Word Size (depends on CPU)")

Space=input("Enter the space in the memory")
Addressability=input("Enter how the memory is addressable (serial number)")
if Addressability=="4":
    wordsize=int(input("Enter cpu-bit size(in bits)"))
else:
    wordsize=0
    
query=input("Enter type of query:1,2a,2b")
if query=="1":
    instnsize=int(input("Enter size of instruction"))
    reglen=int(input("Enter length of registers"))
    
    dict={"M":20,"k":10,"G":30}

    s=0
    for i in range(0,len (Space)-2):
        s=s*10+int(Space[i])
    a=round(log(s,2)+dict[Space[-2]])
    bits=Space[-1]
    if bits=='B':
        Adrress={'byte':0,'nibble':-1,'bit':-3,'word':wordsize}
        if Addressability=="word":
            Adrress['word']=round(log(wordsize/8,2))
        P=a-Adrress[Addressability]
    else:
        Adrress={'byte':3,'nibble':2,'bit':0,'word':wordsize}
        if Addressability=="word":
            Adrress['word']=round(log(wordsize,2))
        P=a-Adrress[Addressability]
    print("Address size: ",P)
    Q=instnsize-reglen-P
    print("Length of opcode: ",Q )
    R=instnsize-2*reglen-Q
    print("No of filler bits: ",R)
    maxinst=2**Q
    print("Maximum no of instruction supported: ",maxinst)
    maxreg=2**reglen
    print("Maximum no of registers supported: ",maxreg)
else:
    sp = int(Space[0:-2])
    if (Space[-2] == 'M'):
        sp *= 2**20
    if (Space[-2] == 'K'):
        sp *= 2**10
    if (Space[-2] == 'G'):
        sp *= 2**30
    if (Space[-1 == 'B']):
        sp *= 8  
    if query == "2a":
        ans = 0
        word = int(input("bits of cpu: "))
        new = int(input("New type of memory"))
        if type == "1":
            if new == "1":
                ans = 0
            elif new == "2":
                ans = -2
            elif new == "3":
                ans = -3
            else:
                ans = -log(word,2)
        elif type == "2":
            if new == "1":
                ans = 2
            elif new == "2":
                ans = 0
            elif new == "3":
                ans = -1
            elif new == "4":
                ans = -log(word,2) + 2
        elif type == "3":
            if new == "1":
                ans = 3
            elif new == "2":
                ans = 1
            elif new == "3":
                ans = 0
            else:
                ans = -log(word,2) + 3
        elif type == "4":
            if new == "1":
                ans = log(word,2)
            elif new == "2":
                ans = log(word,2) - 2
            elif new == "3":
                ans = log(word,2) - 3
            else:
                ans = 0
        print (ans," '+represnt excess & - represent saved'")
    else:
        word = int(input("bits of cpu: "))    
        pins = int(input("no of pins used: "))
        type = int(input("Mention the serial number of current type of memory: "))
        st = pow(2,pins)
        if type == "1":
            if (st >= 2**33):
                i = st/(2**33)
                print(i," GB")
            elif (st >= 2**23):
                i = st/(2**23)
                print (i,"MB")
            elif (st >= 2**13):
                i = st/(2**13)
                print(i," KB")
            elif (st >= 2**3):
                i = st/(2**3)
                print(i," B")
            else:
                print(st," b")
        elif type == "2":
            if (st >= 2**31):
                i = st/(2**31)
                print(i," GB")
            elif (st >= 2**21):
                i = st/(2**21)
                print (i,"MB")
            elif (st >= 2**11):
                i = st/(2**11)
                print(i," KB")
            elif (st >= 2**1):
                i = st/(2**1)
                print(i," B")
            else:
                print(st * 4," b")
        elif type == "3":
            if (st >= 2**30):
                i = st/(2**30)
                print(i," GB")
            elif (st >= 2**20):
                i = st/(2**20)
                print (i,"MB")
            elif (st >= 2**10):
                i = st/(2**10)
                print(i," KB")
            else:
                print(st," B")
        elif type == "4":
            word = log(word,2)
            st = st * 2 **(word-3)
            if (st >= 2**30):
                i = st/(2**30)
                print(i," GB")
            elif (st >= 2**20):
                i = st/(2**20)
                print (i,"MB")
            elif (st >= 2**10):
                i = st/(2**10)
                print(i," KB")
            else:
                print(st," B")