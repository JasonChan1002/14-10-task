def toBinary(x):
    list=[]
    while x!=0:
        z=x%2
        list.append(z)
        x=x//2
        y=''.join(str(list))
    print (y)
num=int(input("enter a integer"))
toBinary(num)
