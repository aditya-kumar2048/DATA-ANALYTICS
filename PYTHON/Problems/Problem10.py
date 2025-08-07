# WAP to check if a number is a single digit number , 
# 2-digit , 3 - digit or so on.... upto 5-digit.

num = int(input("Enter input : "))
if num>0 and num<10 : 
    print("It is single digit number")

elif num>9 and num<100 : 
    print("It is double digit number")
elif num>99 and num<1000 : 
    print("it is three digit number")
elif num> 999 and num<10000 : 
    print("It is four digit number")
elif num> 9999 and num <100000: 
    print("It is five digit number ")
else : 
    print("IT is larger than 5 digit number")