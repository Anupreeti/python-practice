# Create a class Person with name and age
# Add method to greet using that name

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def greet(self):
        return f"Hello {self.name} your age is {self.age}!"

User = Person("Preeti",35)
print(User.greet())
