# Bubble sort (swaps)
# Time complexity = O(nn)
x= [7, 12, 9, 4,0,-1,-12,-92,100,1235,1547465,11]
print(x)
for i in range(len(x)-1):
    swapped=False
    for j in range(len(x)-i-1):
        if x[j]>x[j+1]:
            x[j],x[j+1]=x[j+1],x[j]
            swapped=True
    if not swapped:
        break
print("Bubble_sort",x,"O(nn)")
print("")
