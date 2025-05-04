#string
first_name = "Renny"
food = "burrito"
email = "renny.abraham@gmail.com"

#Integers
age = 40
quantity = 3
num_of_students = 30

#Float
price = 10.99
gpa = 3.2
distance = 5.5

#Boolean
is_student = True


print(first_name)
print(f"Hello {first_name}")
print(f"Your email is {email}")
print(f"You are {age} years old.")
print(f"You are buying {quantity} items")
print(f"Your class has {num_of_students} students.")
print(f"The price is ${price}")
print(f"Your gpa is: {gpa}")
print(f"You ran {distance} kms.")
print(f"Are you a student?: {is_student}")
if is_student:
    print("You are a student")
else:
    print("You are not a student")

#String manipulation
print("Hello world\nHello world\nHello world")
#concatenation
print("Hello"+"Jenny")
print("Hello"+" "+"Jenny")
print("Hello"+""+"Jenny")