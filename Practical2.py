# #Rectangle Pattern
# for i in range(4):
#     for j in range(6):
#         print("*", end=" ")
#     print()



# #Increasing Triangle
# for i in range(1, 8):
#     for j in range(i):
#         print("*", end=" ")
#     print()


# #Number Square
# for i in range(4):
#     for j in range(1, 5):
#         print(j, end=" ")
#     print()


# #Multiplication Tables
# for i in range(1, 11):
#     print(f"--- Table of {i} ---")
#     for j in range(1, 11):
#         print(f"{i} x {j} = {i*j}")
#     print()


# #Classroom Seating
# for row in range(1, 6):
#     for seat in range(1, 9):
#         print(f"R{row}S{seat}", end=" ")
#     print()


# #Prime Numbers
# for num in range(2, 51):
#     is_prime = True
#     for i in range(2, int(num**0.5) + 1):
#         if num % i == 0:
#             is_prime = False
#             break
#     if is_prime:
#         print(num, end=" ")


# #Pattern Challenge
# n = 5
# for i in range(1, n+1):
#     for j in range(n - i):
#         print(" ", end=" ")
#     for k in range(2*i - 1):
#         print("*", end=" ")
#     print()