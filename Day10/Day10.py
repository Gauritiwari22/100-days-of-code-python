"Day10"

# Functions with outputs = using keyword result
def format_name(f_name,l_name):
    if f_name=="" or l_name=="":
        return "You did not enter vaid inputs."
    first=f_name.title()
    last=l_name.title()
    return f"Hello,{first} {last}!"

print(format_name(input("What is your first name?"),input("What is your last name?")))

# To check if entered year is a leap year or not
def is_leap_year(year): 
    
    if year%4==0:
        if year%100==0:
            if year%400==0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

print(is_leap_year(2000))
        
# Docstrings - documentation strings with meaning and that are stored by python.
def is_leap_year(year): 

    """Enter any year you want to check if its leap or not"""

    if year%4==0:
        if year%100==0:
            if year%400==0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False








