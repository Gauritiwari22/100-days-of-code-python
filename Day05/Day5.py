"Day5"

# for loop- iterates over each element in a data structure
fruits=["apple","banana","mango","pear","kiwi"]
for fruit in fruits:
    print(fruit)    # prints a list of all the fruits one by one

student_scores=[98,34,67,33,89,44,90,24,87,23,56,78]
print(sum(student_scores))  #using sum function to print the sum to student scores

# using for loop to print sum 
total=0
for i in student_scores:
    total+=i
print(total)


print(max(student_scores)) # using max function to print the maximum score from the list

# using for loop to print the maximum score
maximum=0
for i in student_scores:
    if i>maximum:
        maximum=i
print(maximum)

# Range function- range(a,b) (b excluded)
for i in range(1,11): #to print a series of numbers from 1 to 10
    print(i)


# to print sum of numbers from 1 to 100
summation=0
for i in range(1,101):
    summation+=i

print(summation)

# to print even numbers
for i in range(1,101,1): #(start,stop+1,step)
    print(i)