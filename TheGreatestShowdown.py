# 2. The Greatest Showdown

# Task 1: Identify the Greatest Write a Python program 
# that asks the user to enter three numbers. Your code 
# should then identify and print out the largest number among the three.

# Task 2: Identify the Smallest Improve upon your code 
# from Task 1 to also determine the smallest number among the three and print it out.

# Expected Outcome: If we provide the numbers 3, 3, and 4, 
# it should print out that "The smallest number is 3. The largest number is 4. "


print("Please provide 3 numbers and I will identify the smallest number and the largest number in the group!")
number_1 = int(input("Please enter the 1st number of the 3 numbers you've chosen: (Please only enter 1 digit numbers) "))
number_2 = int(input("Please enter the 2nd number of the 3 numbers you've chosen: (Please only enter 1 digit numbers)"))
number_3 = int(input("Please enter the 3rd number of the 3 numbers you've chosen: (Please only enter 1 digit numbers)"))

the_greatest_showdown = []
the_greatest_showdown.append(number_1)
the_greatest_showdown.append(number_2)
the_greatest_showdown.append(number_3)

print(f"The smallest number is {min(the_greatest_showdown)}. The largest number is {max(the_greatest_showdown)}")
