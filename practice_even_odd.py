# Create a function to check if a number is even or odd
def check(num):
    if num%2==0:
        return "Number is even"
    return "Number is odd"
num1 = int(input("Eneter any number to check if even or odd: "))
print(check(num1))
