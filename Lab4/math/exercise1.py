import math

def radian_find(n):
    radians = (n * math.pi) / 180
    return radians

n = float(input("Input degree: "))
print("Output radian:" , round(radian_find(n), 6))