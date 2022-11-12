# 1 --> Write a program that calculates the area of a circle with a radius = 5. Use an approximate value of pi:  
  
# pi = 3.14 
# Solution :- 
# pi = 3.14
# r = 5 # redius
# circle = pi * r ** 2
# print(circle)




# 2 --> Write a program that calculates the future value of 1000 USD with an annual interest rate of 3%, annual capitalization and a 5-year investment period. Round the result to the nearest cent.  
# Tip: Use compound capitalization of interest.  
# Print the result to the console as shown below.  
# Expected result:  
# The future value of the investment: 1159.27 USD 
# Solution:- 
# F = P(1+i)^n
# P = 1000
# i =  0.03 # 3% // 100
# n = 5
# F = P * ( 1+i)**n
# print(f"The future value of the investment:- {F:.2f} ")


# Question 3 --> Write a program that calculates the delta for the quadratic equation:
# 3x^2 \ - 4x + 1 = 0
# Print the result to the console as shown below.
# Expected result:

# Delta: 4
# Solution :-
# a = 3
# b = -4
# c = 1
# delta = b**2-4*a*c
# print(f"Delta :- {delta}")


# Question 4 --> The arithmetic sequence is given with the following formula:
# a_n\ =\ 10\ +\ 4n
# Calculate the sum of the first ten elements of this sequence. Print the result to the console as shown below.
# Expected result:
# The sum of the first 10 elements in a sequence: 320.0
# Solution :-
# a_n = 10 + 4 * n = 10 + 4 * 1 = 10 + 4 = 14

# a1 = 14
# a10 = 50
# n = 10
# S10 = ((a1 + a10) / 2) *n
# print(f"The sum of the first 10 elements in a sequence: {S10}")

# Question 5 --> The geometric sequence is given with the following formula:
# a_n = 8 * 2^n-1
# Calculate the sum of the first six elements of this sequence. Print the result to the console as shown below.
# Expected result:
# The sum of the first 6 elements of the sequence is: 504.0
# Solution :- 
# a1 = 8
# a2 = 8 * 2
# n = 6
# S6 = a2/a1
# res =  a1 * (1-S6**n) / (1-S6)
# print(f"The sum of the first 6 elements of the sequence is:- {res}")


# Question 6 -->  The quadratic equation is given with the following formula:
# x^{2\ }+\ 5x\ +\ 4\ =\ 0\ 
# Using Vieta's formulas calculate the sum and product of the roots of this quadratic equation. Print the result to the console as shown below.
# Expected result:
# x1 + x2 = -5.0
# x1x2 = 4.0
# Solution :- 
# a = 1
# b = 5
# c = 4
# summ = -b / a
# product = c / a
# print(f"x1 + x2 = {summ}\nx1x2 = {product}")



# 7 --> Calculate the midpoint of the segment with ends at the points: A = (2, 4), B = (-4, 6) and print result to the console as shown below. 
# Expected result: 
# The middle point: (-1.0, 5.0) 
# Solution :- 
# a1 = 2
# a2 = 4
# b1 = -4
# b2 = 6
# A = (a1+b1) / 2
# B = (a2 + b2) / 2
# print(f"The middle point of A and B is :- {A,B}")


# 8 --> Calculate the distance of two points A = (3, 2), B = (- 1, -1) and print result to the console as shown below. 
# Expected result: 
# The distance between points A and B: 5.0 
# Solution:- 
# a1 = 3
# a2 = 2
# b1 = -1
# b2 = -1
# Distance = ((a1-b1)**2 + (a2-b2)**2)**(1/2)
# print(f"The distance between points A and B:- {Distance}")


# Question 9 -->  Find the roots of the quadratic equation:
# x^{2\ }+\ 5x\ +\ 4\ =\ 0\ 
# Print the result to the console as shown below.
# Expected result:
# x1 = -4.0
# x2 = -1.0
# Solution:- 
# a = 1 
# b = 5
# c = 4
# delta = b**2 - 4*a*c
# delta_sqrt = delta ** (1/2)
# X = (-b - delta_sqrt) / (2 * a)
# Y = (-b + delta_sqrt) / (2 * a)
# print(f"x1 = {X}\nx2 = {Y}")



# 10 --> Calculate the geometric mean of the following numbers: 4, 3, 4.5, 5 and print result to the console as shown below.  
# Expected result:  
# Geometric average of the given numbers: 4.05 
# Solution :- 
# a,b,c,d = 4, 3, 4.5, 5 
# geo_mean = (a * b * c * d) ** (1/4)
# print(f"Geometric average of the given numbers :- {geo_mean:.2f}")


# 11 --> Calculate the standaard deviation of the following set of data: 10, 11, 9.    
# Print the result to the console as shown below.  
# Expected result:  
# The standard deviation: 0.82
# Solution:- 
# a , b, c = 10 , 11 ,9
# mean = (a + b + c) / 3.0
# Deviation = ((a-mean)**2 + (b-mean)**2 + (c - mean)**2) / 3.0
# standaard_deviation = Deviation ** (1/2)
# print(f"The standard deviation :- {standaard_deviation:.2f}")


# Question 12 -->  An infinite geometric sequence is given with the following formula:
# 1\ ,\ \frac{1}{2}\ ,\ \frac{1}{4}\ ,\ \frac{1}{8}\ ,....
# Calculate the sum of this sequence. Print the result to the console as shown below.
# Expected result: - 2.0

# # Solution:- 
# a1 = 1
# a2 = 1/2
# geo = a2 / a1
# Seq = a1 / (1-geo)
# print(f"Sequence: - {Seq}")


# The sum of the sequence: 2.0