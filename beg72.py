z=list(input())
q=['a','e','i','o','u']
for i in range(len(z)):
    if z[i] in q:
        print("yes")
        break
else:
    print("no")
        
