def findFirst(y):
    for x in range(10):
        if y[x][2]==0:
            print ("section ",(x+1),"are free")
            return "0"
        else:
            return "-1"
con=True
rows, cols=(10,3)
z=0
list2=[]
time=["9:00","9:30","10:00","10:30","11:00","11:30","13:00","13:30","14:00","14:30"]
list = [[0]*cols for _ in range(rows)]
for x,z in zip(range(10),time):
    list[x][0]=x+1
    list[x][1]=z
    y=list[x]
    print (list[x])
    list2.append(y)
while con==True:
    findFirst(list2)
    userin=int(input("enter the section that u want to book"))
    if list2[(userin-1)][2]==0:
        ID=str(input("enter your customer ID"))
        list2[userin-1][2]=ID
        print (list2)
        con=False
    else:
        con=True
        print ("that section has already book")