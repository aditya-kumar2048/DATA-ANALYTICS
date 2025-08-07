#WAP to create area calculator

print("********AREA CALCULATOR*********")

print("""PRESS 1  to get the area of square 
      PRESS 2 to get area of rectangle 
      PRESS 3 to get area of cicle 
      press 4 to get the area of triangle""")

choice = int (input("enter a number between 1-4 : "))

if choice == 1 : 
        side = float(input("enter the length of one side : "))
        area = side**2 ; 
        print("The area of Square is : ", area)

elif choice ==2 : 
        L = float(input("Enter the length of rectangle : "))
        B = float(input("Enter the breadth of rectangle : "))
        area  = 2*(L + B)
        print("The area of rectangle is : ",area)
  

elif choice ==3 : 
        rad = float(input("Enter the radius of circle : "))
        pi = 3.1415
        area = pi * rad * rad
        print("The area of circle is : ",area)
elif choice == 4 : 
        B = float(input("Enter the Base of triangle  : "))
        H = float(input("Enter the height of triangle : "))

        area = .5 * B * H
        print("The area of triangle is : " , area)

else : print("Invalid choice.")