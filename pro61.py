vj=list(map(str,input()))
vk=list(map(str,input()))
for j in range(0,len(vk)):
    m=r=l=0
    r=ord(vj[j])
    l=ord(vk[j])
    m=r+l
    if m>96 and m<123:
        print(chr(m),end="")
    elif (m-96)<122 and(m-96)>96:
        m=m-96
        print(chr(m),end="")
    elif m>148:
        m=m-96-26
        print(chr(m), end="")
    else:
        m=m-26
        print(chr(m), end="")
