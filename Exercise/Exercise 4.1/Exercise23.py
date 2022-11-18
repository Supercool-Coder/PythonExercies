# Question 2 :- 

# From the following text:
# string = 'PKV-89415-PLN'

# extract the code containing the first three and last three characters. Print the result to the console.

# Expected result:
# PKVPLN

# Solution :- 
string = 'PKV-89415-PLN'
code = string[:3] + string[10:]
print(code)