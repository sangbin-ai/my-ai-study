total=0
for i in range(1, 11):
    total += i
    
print("총합:",total)

for i in range(2, 10):
    for j in range(1, 10):
        print(i, "x", j, "=", i * j)

for x in range(1, 4):
    for y in range(1, 4):
        print((x, y))

for i in range(5, 0, -1):
    print("★" * i)






for i in range(1, 6):
    print(" "*(5-i)+"★"*(2*i-1))

x=7
for i in range(1, 6):
    for j in range(1, 6):
        if j == 1 or j == (2*i - 1):
            print()

 