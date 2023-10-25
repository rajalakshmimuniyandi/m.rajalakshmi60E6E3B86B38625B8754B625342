 # python program for linear search using for loop

#define list
lst = []

#take input list size
num = int(input("Enter size of list :- "))

for n in range(num):
    #append element in list/array
    numbers = int(input("Enter the array of %d element :- " %n))
    lst.append(numbers)

#take input number to be find in list   
x = int(input("Enter number to search in list :- "))

# Recursive function to linear search x in arr[l..r]  
def recLinearSearch( arr, l, r, x): 
    if r < l: 
        return -1
    if arr[l] == x: 
        return l 
    if arr[r] == x: 
        return r 
    return recLinearSearch(arr, l+1, r-1, x) 

res = recLinearSearch(lst, 0, len(lst)-1, x) 

if res != -1:
  print('{} was found at index {}.'.format(x, res))
else:
  print('{} was not found.'.format(x))

