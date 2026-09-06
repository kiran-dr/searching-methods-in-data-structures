# Selection sort
# Time complexity = O(nn)
# Two Methods 1. pop lowest and insert at current index 2. swap the lowest and current """

# Method 1 it will shift entire remaining elements on each itterations
x= [7, 12, 9, 4,0,-1,-12,-92,100,1235,1547465,11]
print(x)
for i in range (len(x)-1):
    min_index=i
    for j in range(i+1,len(x)):
        if x[j]<x[min_index]:
            min_index=j
    min_value=x.pop(min_index)
    x.insert(i,min_value)
print("selection_sort",x)
print("")

# Method 2 swap the lowest and current
x= [7, 12, 9, 4,0,-1,-12,-92,100,1235,1547465,11]
print(x)
for i in range (len(x)-1):
    min_index=i
    for j in range(i+1,len(x)):
        if x[j]<x[min_index]:
            min_index=j
    x[i],x[min_index]=x[min_index],x[i]
print("Updated selection_sort",x,"O(nn)")
print("")
