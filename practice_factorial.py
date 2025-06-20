# Write a function that returns the factorial of a number
num2 = int(input("Enter a number to check factorial= "))
def factorial(num): #4*3*2*1
    i=1
    fact=1
    while i<=num:
        fact=i*fact
        i=i+1
    print(f"factorial of {num} is = {fact}")
factorial(num2)
