from math import factorial
n=int(input("enter the nmber of rows="))
for i in range(n):
    for j in range(n-i+1):
        print(end="")
    for j in range(i+1):
        print(factorial(i)//factorial(j)*factorial(i-j),end="")
    print()
    
