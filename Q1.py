print ("enter 1 to 100. If number could divid by 3, enter'fizz'. If number could divid by 5, enter 'buzz'. If both, enter 'fizz buzz'")
for x in range(1,101):
    userin=str(input("enter number, fizz or buzz"))
    if (x%3)==0 and (x%5)!=0:
        y="fizz"
    elif (x%5)==0 and (x%3)!=0:
        y="buzz"
    elif (x%3)==0 and (x%5)==0:
        y="fizz buzz"
    else:
        y=str(x)
    if userin==y:
        print ("correct")
    else:
        print ("wrong, the anser is:", y)
