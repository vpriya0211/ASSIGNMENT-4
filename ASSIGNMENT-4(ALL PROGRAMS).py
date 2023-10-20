# A Python program to create a lambda function that adds 25 to a given number passed in as an argument.

add = lambda num: num + 25
number = int(input("Enter a number: "))
result = add(number)
print("Result:", result)

# A Python program to triple all numbers of a given list of integers. Use Python map.

input_list = list(map(int,input("Enter the numbers: ").split()))
result = list(map(lambda n:n*3,input_list))
print("Result:",result)

# A Python program to square the elements of a list using map() function.

input_list = list(map(int,input("Enter the numbers: ").split()))
result = list(map(lambda n:n**2,input_list))
print("Result:",result)
