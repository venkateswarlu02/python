n=int(input("enter the number"))
for i in range(1,n+1):
    if i%3==0 and i%5==0:
        print("ffizzBUZZ")
    elif i%3==0 and i%5!=0:
        print("fiZZ")
    elif i%5==0 and i%3!=0:
        print("buZZ")
    else:
        print(i)
