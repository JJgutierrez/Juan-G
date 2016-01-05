count  = 1
r = input("type a number")
r = int(r)
for i in range(r+1):
    for j in range(0, i):
	    print ( '*', end='')
	    count = count + 1
    print() 