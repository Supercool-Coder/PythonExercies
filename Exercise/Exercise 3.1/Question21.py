# Question 11 -->  An infinite geometric sequence is given with the following formula:
# 1\ ,\ \frac{1}{2}\ ,\ \frac{1}{4}\ ,\ \frac{1}{8}\ ,....
# Calculate the sum of this sequence. Print the result to the console as shown below.

# Expected result:


# The sum of the sequence: 2.0
# 	• exercise.py
a1 = 1
a2 = 1/2
q = a2 / a1
S = a1 / (1 - q)
print(f'The sum of the sequence: {S}')