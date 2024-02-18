n = int(input())

c = (i for i in range(n+1) if i%2==0)
for s in c:
    print(s, end=",")