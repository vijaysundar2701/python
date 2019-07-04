vj,vk = map(int,input().split())
nk = list(map(int,input().split()))
az = int(input())
lm = (sum(ms)-ms[vk])//2
if az == lm:
  print("Bon Appetit")
else:
  print(az-lm)
