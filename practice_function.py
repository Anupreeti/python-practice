def greet(name="friend"):
    return f"Hello {name}"

print(greet("Preeti"))
print(greet())

# Write a function to return square of a number
def square(num):
    return num**2

print(square(int((input("Eneter a number to get square of: ")))))

# Write a function that takes a list and returns only even numbers [22,3,4,5,3,33,4,4,5,5,555]
def even_num(numbers):
    '''This function will get list of integers
    and then return anoth list with even numbers'''
    even = []
    for i in numbers:
        if i%2==0:
            even.append(i)
    return even
input_num = input("Enter numbers seprated by spaces: ")
numbers = list(map(int,input_num.split()))
print(even_num(numbers))
