"Day2"

# Subscripting- returns the element at a particular position
print("hello"[0]) #prints first element i.e h
print("hello"[2]) #prints third element i.e l
print("hello"[-1]) #print last element i.e o

# Data types

#String- enclosed within quotes
name="hello"
place="Mumbai"

#integer- whole numbers, no decimals
num=4
nums=8473783

#float- decimal numbers
num1=3.7384
num2=173.39273

#boolean- True, False
is_happy=True
is_alive=False

#Type function- checks the data type
print(type(num))
print(type(num2))

#Type conversion
a=int("5")
print(type(a))

b=bool("False")
print(type(b))

# Mathematical operation
print(3+5)
print(8-3)
print(8*3)
print(6/3) #prints float value
print(6//3) #prints integer value
print(2**6)


#operator precedence- checks which mathematical operation to be performed first
#follows PEMDAS i.e parenthesis,exponent,multiplication/division,addition/subtraction
#multiplication/division and addition/subtraction is decided by moving from left to write in the question

print(3*3+3/3-3)
#output=7

#round function
print(round(4.6378))
print(round(526.773,2))

#assignemt operator
i=0
i+=1 #increments value of i by 1
print(i) #output=1

#similarly -=,*=,/=

#F string- does not require type conversion to concatenate
name="Gauri"
score="98"
print(f"{name} scored {score}")



