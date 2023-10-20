# A Python program to square the elements of a list using map() function.

input_list = list(map(int,input("Enter the numbers: ").split()))
result = list(map(lambda n:n**2,input_list))
print("Result:",result)