a=list(map(int,input("enter a list of numbers seperated by space:").strip().split()))
b=list(map(int,input("enter a list of numbers seperated by space:").strip().split()))
print("the list 1 is:"+str(a))
print("the list 2 is:"+str(b))
size_1=len(a)
size_2=len(b)
res=[]
i,j=0,0
while i<size_1 and j<size_2:
    if a[i]<b[j]:
        res.append(a[i])
        i+=1
    else:
        res.append(b[j])
        j+=1
res =res+a[i:]+b[j:]
print("the combained sorted listis:" + str(res))





















      
