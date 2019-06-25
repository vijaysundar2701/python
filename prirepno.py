x=int(input())
y=input()
z=''
for i in y:
    if i in z and i!=" ":
        print(int(i))
        break
    else:
        z+=i
if z==y:
    print("unique")
