print("which multiplication table do you want:")
d=int(input())

a=1

for i in range ( d, d*10+1, d):
    print (d, "x", a, "=", i)
    a = a+1
