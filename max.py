#finding maximum element in an array

a=[1,2,1,2,3,4,5,6,6,7,7]
max=a[0]
for i in a:
    if i>max:
        max=i
print(max)