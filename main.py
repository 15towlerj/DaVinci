n = 0
x = 1
y = 0
flip = 0
print ("1")
while (n != 20):
    if (flip == 0):
        print (x+y)
        y = y+x
        n= n+1
        flip = 1


    else:
        print (x+y)
        x = x+y
        n = n+1
        flip = 0




