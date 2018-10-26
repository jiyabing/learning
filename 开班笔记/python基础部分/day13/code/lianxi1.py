fx = lambda n:(n**2+1)%5 == 0
print(fx(4))
print(fx(2))


#mymax = lambda *args: max(args)
mymax = lambda x,y:x if x>y else y
print(mymax(1,2))
