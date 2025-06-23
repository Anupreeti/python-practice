with open("todo.txt","w") as f:
    f.write("Hello Preeti!")

with open("todo.txt","r") as f:
    data=f.read()
    print(data)

with open("todo.txt","a") as f:
    f.write("\nPrint python code")

with open("practice.txt","w") as f:
    f.write("Hello World! \nWe are learning Python \nI will save this file \n")

with open("practice.txt","r") as f:
    data=f.read()
    print(data)

with open("practice.txt","a") as f:
    f.write("Append data in this file")
