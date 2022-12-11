# Question 2 :- The following tuples are given:


# dji1 = ('AAPL.US', 'IBM.US', 'MSFT.US')
# dji2 = ('HD.US', 'GS.US', 'NKE.US')

# Nest these tuples into one tuple as shown below and print the result to the console.

# Expected result:
# (('AAPL.US', 'IBM.US', 'MSFT.US'), ('HD.US', 'GS.US', 'NKE.US'))


# Question 3 :- Tuples are immutable. The following tuple is given:

# members = (('Kate', 23), ('Tom', 19))

# Insert a tuple ('John', 26) between Kate and Tom as shown below. Print the result to the console.

# Tip: You have to create a new tuple.

# Expected result:


# (('Kate', 23), ('John', 26), ('Tom', 19))

# Solution :- 

members = (('Kate', 23), ('Tom', 19))
members = (members[0], ('John', 26),members[1])
print(members)