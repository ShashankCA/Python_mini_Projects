print("  SIMPLE CALCULATOR  ")

print("1 . Add ")
print("2 . Subtract ")
print("3 . mutiply ")
print("4 . Division")

choice = input("Enter you choice from 1 to 4: ")

num1 = int(input("enter the first number: "))
num2 = int(input("enter the second number: "))

if choice == 1:
    result = num1+num2
    print(f"The sum of the numbers is {result}")
elif choice == 2:
      result = num1-num2
      print(f"The Difference of the numbers is {result}") 
elif choice == 3:
      result = num1*num2
      print(f"The Product of the numbers is {result}") 
elif choice == 4:
      if num2 != 0:
            result = num1//num2
            print(f"The Quotient of the numbers is {result}") 
      else:
            print("Pls enter non zero number ")
else:
      print("Invalid choice pls select between 1 and 4 ")