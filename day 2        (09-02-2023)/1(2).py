year=int(input("enter the year"))
if year%400==0:
    print('leaf year')
elif year%4==0:
    print('leaf year')
elif year%100==0:
    print('not a leaf year')
else:
    print('not a leaf year')
