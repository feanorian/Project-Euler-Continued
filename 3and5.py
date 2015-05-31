#list all multiples of 3 and 5 from 0 to 1000 and return the sum

'''This function checks to see if numbers are multiples of 3 or 5'''
def mult(a_number):
    if a_number % 3 == 0 or a_number % 5 == 0:
        print a_number
        return True
    else:
       return False

'''appends item to array'''
def append_array(newarray,x):
    newarray.append(x)
    return newarray

'''sums all the numbers'''
def arraysum(array):
    m=0
    for i in array:
        m += i
    print m

myarray=[]

#this is where the magic happens
for i in range(101):
    mult(i)
    if multi(i) == True:
        append_array(myarray,i)
arraysum(myarray)








