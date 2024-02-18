def squares(a, b):
    for num in range(a, b + 1):
        yield num ** 2

a = int(input())
b = int(input())
for items in squares(a, b):
    print(items)