"Day12"

# Scope - local scope and global scope (Namespace)

# Local scope includes variables defined inside a function and they are only valid till inside a function
# Global scope includes variables defined outside a function and they can be read inside the function as well

apples=5 #global scope

def num_apples():
    apples=6 #local scope
    print(f"Number of apples={apples}")

num_apples()
print(f"Number of apples={apples}")


# To check if a number is prime or not
def is_prime(num):
    if num==2:
        return True
    if num==1:
        return False
    for i in range(2,num):
        if num%i==0:
            return False
        
    return True

print(is_prime(25))

# Modifying global scope
apples=5 

def num_apples():
    global apples
    apples+=1 # The global scope variable gets modified
    print(f"Number of apples={apples}")

num_apples()
print(f"Number of apples={apples}")

# Global Constants - values that are never changed - denoted with capital letters
PI=3.14159
G=6.67*10^-11

# These values now can never be modified inside a function

