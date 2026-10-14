# #Greeting Function
# def greet(name):
#     print(f"Welcome, {name}!")

# greet("Aman")


# #Addition Function
# def add(a, b):
#     return a + b

# print(add(5, 10)) # 15


# #Even Or Odd
# def check_even_odd(n):
#     if n % 2 == 0:
#         return "Even"
#     else:
#         return "Odd"

# print(check_even_odd(7)) # Odd


# #Factorial Calculator
# def factorial(n):
#     fact = 1
#     for i in range(1, n+1):
#         fact *= i
#     return fact

# print(factorial(5)) # 120


# #Largest of three numbers
# def largest(a, b, c):
#     if a >= b and a >= c:
#         return a
#     elif b >= c:
#         return b
#     else:
#         return c

# print(largest(10, 25, 15)) # 25


# #Grade Calculator
# def get_grade(marks):
#     if marks >= 90:
#         return "A+"
#     elif marks >= 80:
#         return "A"
#     elif marks >= 70:
#         return "B"
#     elif marks >= 60:
#         return "C"
#     elif marks >= 33:
#         return "D"
#     else:
#         return "Fail"

# print(get_grade(85)) # A


# #List Statistics
# def total(lst):
#     return sum(lst)

# def average(lst):
#     return sum(lst) / len(lst)

# def minimum(lst):
#     return min(lst)

# def maximum(lst):
#     return max(lst)

# marks = [80, 90, 75, 85]
# print(total(marks), average(marks), minimum(marks), maximum(marks))


#Banking Application

# balance = 45000

# def deposite(amount):
#     global balance
#     if amount > 0:
#         balance += amount
#     else:
#         print("Invalid amount")

# def withdraw(amount):
#     global balance
#     if 0 < amount <= balance:
#         balance -= amount
#     else:
#         print("Invalid amount or insufficient balance")

# def show_balance():
#     print("Balance =", balance)

# while True:
#     print("\n Banking Menu")
#     print("1. Deposite")
#     print("2. Withdraw")
#     print("3. Balance")
#     print("4. Exit")

#     choice = int(input("Enter choice: "))

# if choice == "1":
#     deposite(float(input("Enter amount")))
# elif choice == "2":
#     withdraw(float(input("Enter amount: ")))
# elif choice == "3":
#     show_balance()
# elif choice == "4":
#     print("Thank you for banking with us!")
# else:
#     print("Invalid choice. Please try again.")


# #Student record processor
# students = [
#     {"name": "Aman", "marks": 85},
#     {"name": "Riya", "marks": 32},
#     {"name": "Ankit", "marks": 78}
# ]

# def calculate_average(student_list):
#     total = sum(s["marks"] for s in student_list)
#     return total / len(student_list)

# def get_passing_students(student_list):
#     passing = []
#     for s in student_list:
#         if s["marks"] >= 33:
#             passing.append(s["name"])
#     return passing

# print("Average:", calculate_average(students))
# print("Passing Students:", get_passing_students(students))
