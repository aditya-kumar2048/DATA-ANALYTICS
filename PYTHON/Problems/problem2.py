# write a program to swap two variables

x = 12
y = 13
temp = x
print (temp)

x = y
print(x )
y = temp

print(y)
print("value of x is ", x )
print("value of y : ",y)

# Method 2

a = 30 
b = 40

# left, right = right , left
a,b = b , a 
print ("the value of b :",b)
print("the value of a : ",a)