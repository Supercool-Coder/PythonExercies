# 2 --> Write a program that calculates the future value of 1000 USD with an annual interest rate of 3%, annual capitalization and a 5-year investment period. Round the result to the nearest cent.  
  
  
  
# Tip: Use compound capitalization of interest.  
  
  
  
# Print the result to the console as shown below.  
  
  
  
# Expected result:  
  
  
  
# The future value of the investment: 1159.27 USD 


#  Formula = F = P(1+i)^n

P = 1000
i = 0.03 + 1
n = 5
F = P * i ** n
print(f"The future value of the investment: {F:.2F} USD")