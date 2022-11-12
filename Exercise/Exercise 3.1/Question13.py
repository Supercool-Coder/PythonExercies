# Question 4 --> The arithmetic sequence is given with the following formula:
# a_n\ =\ 10\ +\ 4n
# Calculate the sum of the first ten elements of this sequence. Print the result to the console as shown below.

# Expected result:


# The sum of the first 10 elements in a sequence: 320.0

# Find the First 10th element :-
# for a1 -> 1 ==>  10 + 4 x 1 = 14
# for a2 -> 2 ==>  10 + 4 X 2 = 18
# for a3 -> 3 ==>  10 + 4 X 3 = 22
# for a4 -> 4 ==>  10 + 4 X 4 = 26
# for a5 -> 5 ==>  10 + 4 X 5 = 30
# for a6 -> 6 ==>  10 + 4 X 6 = 34
# for a7 -> 7 ==>  10 + 4 X 7 = 38
# for a8 -> 8 ==>  10 + 4 X 8 = 42
# for a9 -> 8 ==>  10 + 4 X 9 = 46
# for a10 -> 8 ==>  10 + 4 X 10 = 50

# If we add add these values then we also find the solution .

a1 = 14
a10 = 50
n = 10

# This sum can be found quickly by taking the number n of terms being added 
# (here 10), multiplying by the sum of the first and last number in the progression 
# (here 14 + 50 = 64), and dividing by 2:

Element_10 = ((a1+a10) / 2) * n
print(Element_10)