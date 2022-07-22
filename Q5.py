from email.headerregistry import Address
import math

Space=input("Enter the space in the memory")
Addressability=input("Enter how the memory is addressable")
if Addressability=="word":
    wordsize=int(input("Enter word size(in bits)"))
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
    a=round(math.log(s,2)+dict[Space[-2]])
    bits=Space[-1]
    if bits=='B':
        Adrress={'byte':0,'nibble':-1,'bit':-3,'word':wordsize}
        if Addressability=="word":
            Adrress['word']=round(math.log(wordsize/8,2))
        P=a-Adrress[Addressability]
    else:
        Adrress={'byte':3,'nibble':2,'bit':0,'word':wordsize}
        if Addressability=="word":
            Adrress['word']=round(math.log(wordsize,2))
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
    
    
        


