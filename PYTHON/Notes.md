1. for the next line there are two methods :-
    i) use of triple quotation symbol eg - (""" hii 
                                            this is 
                                                Aditya """)

    ii) use of backslash n (\n) eg - ("this is \n Aditya")

2. Comments in python :-
    . To add single line comments , # hash is used
    .  to add multiline comments , triple quotations are used

3. Python is case sensative

4. Rules for writing  a variables
    . Python is case - sensitive language , therefore the variables names are case sensitive as well.

          Input - 
             A = "hello"
               print(a)
              Output - 
              It will throw an error as the cases used here for variable's name is different.  
    . Make sure to not use spaces while creating a variable.
    One can use (_) underscore to separate the names while writting a variable

    . A variable name should never start with a number or special symbols.


# Datatypes : 
- Text-type : String(str)
- Numeric Types : integer(int), floating (float), complex
- Sequence Types : list , tuple and range 
- Mapping Type : Dictionaries (dict)
- Set Type : set, frozenset
- Boolean Type : bool
- Binary Types : Bytes , bytearray , memoryview

# User-inputs
----> To ask for the input from the user. Default datatype is string.

`Input` 
Name = input("enter your name here")
print(Name)

`Output:`
Entered name by the user 


# Operators and Operands:
   Operators indicates what operation is to be performed while Operands indicates on what the action or the operation should be performed .

   x + y = 0
   in the given expression , x , y, and 0 are Operands and +  , = are operators

  # Types of operators:

Operators can be further divided into 6 categories:

1. Arithmetic operators

2. Comparison Operators

3. Logical Operators

4. Assignment Operators

5. Identity Operators

6. Membership Operators

7. Bitwise Operators
---

1. Arithmetic Operator : 
    - Addition(+)
    - Substraction(-)
    - Division(/)
    - Multiplication(*)
    - Floor division(//)
    - Exponentiation(**)
    - Modulus (%)

2. Comparison Operators : 
    - Less than(<)
    - Less than or Equal to (<=)
    - Not Equal to (!=)
    - Equal to (==)
    - Greater Than(>)
    - Greater Than or Equal to (>=)

3. Logical Operators : 
      Operator    Meaning                                         Example
      and       True if both the operands are true                x and y
      or        True if either of the operands is true             x or y
      not       True if operand is false (complements the operand) not x

4. Assignment Operators :

- Assignment operators are used in Python to assign values to variables.
- a = 6 is a simple assignment operator that assigns the value 6 on the right to the variable a on the left.

Operator                  Example                Equivalent to
   =                       x = 6                    x = 6
   +=                      x+= 6                    x = x + 6
   -=                      x = 6                    x = x - 6
   *=                      x*= 6                    x = x * 6

5. Identity Operator
  
  - Identity operators are used to compare items to see if they are the same object with the same memory address.
   Types : 
   1. Is 
   2. Is not


6. Bitwise Operators :
    These Operators are used to compare the binary numbers 
   - Types : 
      1. AND(&) Operator
      2. OR(|) Operator
      3. XOR(^) Operator
      4. << zero fill left shift
      5. >> zero fill right shift



7. Membership Operators
   Membership operators are used to check the presence of a sequence in an object .
       Types : 
           1. In
           2. not in
---
# Conditional Statements
    Conditional statement allows computer to execute a certain condition only if it is true.

    Types of Conditional Statements: 
        1. If the statement
        2. If-else statement
        3. If-elif-else statement
        4. Nested Statement
        5. Short Hand if Statement

1. If the Statement

    The if statement is the most fundamental decision-making statement .
    The if statement in Python has the subsequent syntax: 
    if expression : 
         statement
 2. If-Else Statement 

    If-else statement is used when you want to give two condition to the computer.
    Here if one condition is false, program executes the another condition.

        if condition : 
                #Will executes this block if the condition is true
        else : 
                #will executes this block if the condition is false
3. If-elif-else Statement 

    In this case , the if condition is evaluated first. if it is false , the elif statement will be executed , if it also comes false then else statement will be executed.
    For multiple condition , more elif statement are added.
    if condition: 
        Body of if
    elif condition : 
        Body of elif
    else Condition : 
        Body of else
4. Nested if Statement 

    A nested if statement if one in which an if statement is nestled inside another if statement . This is used when a variable must be processed more than once. The Nested if statement in Python has the following syntax : 
        if(condition 1 ):
            #Executes if condition 1 is true 
        if(condition 2): 
            #Executes if condition 2 is true 
          #condition 2 ends here
        #condition 1 ends here  

5. Short Hand if Statement

    Short Hand if statement is used when only one statement needs to be executed inside the if block . This statement can be mentioned in the  same line which holds the if statement.
    The short hand if statement in python has the following syntax : 
        if Condition : statement

6. Short Hand if-else statement
    It is used to mention If-else statement in one line in which there is only one statement to execute in both if and else blocks. In simple words , if you have only one statement to execute , one for if , and one for else , you can put it all on the same line.

# Problems 
    1. WAP  to check if a number is positive.
    2. WAP  to check whether a number is odd or even.
    3. WAP to create area calculator
    4. WAP to check whether the passed letter is a vowel or not.
    5. WAP to check if a number is a single digit number , 2 digit number and so on... , upto 5 digits.