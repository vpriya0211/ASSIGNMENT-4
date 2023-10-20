# A Python program to triple all numbers of a given list of integers. Use Python map.

input_list = list(map(int,input("Enter the numbers: ").split()))
result = list(map(lambda n:n*3,input_list))
print("Result:",result)