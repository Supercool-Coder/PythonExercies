# Question 9 -->  Find the roots of the quadratic equation:
# x^{2\ }+\ 5x\ +\ 4\ =\ 0\ 

# Print the result to the console as shown below.

# Expected result:


# x1 = -4.0
# x2 = -1.0
# 	• exercise.py
a = 1
b = 5
c = 4
delta = b ** 2 - 4 * a * c
print(delta)
delta_sqrt = delta ** (1/2)
print(delta_sqrt)
x1 = (-b - delta_sqrt) / (2 * a)
x2 = (-b + delta_sqrt) / (2 * a)
print(f'x1 = {x1}')
print(f'x2 = {x2}')