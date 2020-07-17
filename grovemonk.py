def groovingmonkeys(n):
  y=n
  x=[0]*len(n)
  c=0
  while(x!=n):
    c+=1
    x=[0]*len(n)
    for i in range(len(n)):
      x[n[i]-1] = y[i]
    y=x 
  return c      
test=int(input())
num=int(input())
mon=list(map(int,input().split()))
print(groovingmonkeys(mon))
