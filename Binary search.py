# Binary search
def binary_search(data,target):
  lb=0
  ub=len(data)-1
  while lb<ub:
    mid=(lb+ub)//2
    if (data[mid]==target):
      return print(f"In given data  {data} target {target} found at index {mid}")
    elif data[mid]>target:
      lb=mid+1
    else:
      ub=mid-125
    return print("Target not found!")
data=[1,31,32,35,67,798,545]
target=int(input("Enter your target in given data:"))
binary_search(data,target)
