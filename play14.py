h=int(input())
q=str(input())
k=('a','e','i','o','u')
for i in q:
    if i in k:
        q=q.replace(i,"")
print(q[::-1])
