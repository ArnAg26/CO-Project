from math import *

print("--------------------4 Types of Memory--------------------------------")
print("1. Bit Addressable Memory    - Cell Size = 1 bit")
print("2. Nibble Addressable Memory - Cell Size = 4 bit")
print("3. Byte Addressable Memory   - Cell Size = 8 bits(standard)")
print("4. Word Addressable Memory   - Cell Size = Word Size (depends on CPU)")

Space=input("Enter the space in the memory ")
Addressability=input("Enter how the memory is addressable ")
if Addressability=="4":
    wordsize=int(input("Enter cpu-bit size(in bits) "))
else:
    wordsize=0
    
print("-----------------Types of Query---------------------------")
print("1  : ISA and Instructions related")
print("2a : System enhancement related :: Changing type of memory")
print("2b : System enhancement related :: Size of memory")
query=input("Enter type of query:1,2a,2b ")
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
        Adrress={'1':-3,'2':-1,'3':0,'4':wordsize}
        if Addressability=="4":
            Adrress['4']=round(log(wordsize/8,2))
        P=a-Adrress[Addressability]
    else:
        Adrress={'1':0,'2':2,'3':3,'4':wordsize}
        if Addressability=="4":
            Adrress['4']=round(log(wordsize,2))
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
    if P<1 or Q<1 or R<0:
        print("Values can't be negative")
else:
    sp = int(Space[0:-2])
    if (Space[-2] == 'M'):
        sp *= 2**20
    elif (Space[-2] == 'k'):
        sp *= 2**10
    elif (Space[-2] == 'G'):
        sp *= 2**30
    if (Space[-1] == 'B'):
        sp *= 8  
    if query == "2a":
        ans = 0
        word = int(input("bits of cpu: "))
        new = (input("New type of memory "))
        if Addressability == "1":
            if new == "1":
                ans = 0
            elif new == "2":
                ans = -2
            elif new == "3":
                ans = -3
            else:
                ans = -log(word,2)
        elif Addressability == "2":
            if new == "1":
                ans = 2
            elif new == "2":
                ans = 0
            elif new == "3":
                ans = -1
            else:
                ans = -log(word,2) + 2
        elif Addressability == "3":
            if new == "1":
                ans = 3
            elif new == "2":
                ans = 1
            elif new == "3":
                ans = 0
            else:
                ans = -log(word,2) + 3
        else:
            if new == "1":
                ans = log(word,2)
            elif new == "2":
                ans = log(word,2) - 2
            elif new == "3":
                ans = log(word,2) - 3
            else:
                ans = 0
        print (ans," ('+represnt excess & - represent saved')")
    else:
        word = int(input("bits of cpu: "))    
        pins = int(input("no of pins used: "))
        type = (input("Mention the serial number of current type of memory: "))
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
                print(i," kB")
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
                print(i," kB")
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
                print(i," kB")
            else:
                print(st," B")
        else:
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
                print(i," kB")
            else:
                print(st," B")
