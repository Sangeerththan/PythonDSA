#IIFE of lambda fn
fn = (lambda x: x*x+3)(2)
print(fn)\

## Filter with lambda fn
list_1 = [1,2,3,4,5,6,7,8,9]
filter(lambda x: x%2==0, list_1)    #filter will return an object and must be coverted to list
res=list(filter(lambda x: x%2==0, list_1))
print(res)

#map will perform an operation on the elements of list
list_1 = [1,2,3,4,5,6,7,8,9]
cubed = map(lambda x: pow(x,3), list_1)
cubes=list(cubed)
print(cubes)

