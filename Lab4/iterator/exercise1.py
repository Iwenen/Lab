n = int(input())

c = (i**2 for i in range(n+1))
for s in c:
    print(s)
    