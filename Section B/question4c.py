# importing modules
import math

X1 = int(input('Enter the value of X1:\t'))  
X2 = int(input('Enter the value of X2:\t'))
Y1 = float(input('Enter the value of Y1:\t'))  
Y2 = float(input('Enter the value of Y2:\t'))

# simplified expression
simpleExpression = (X1 - X2) + (Y1 - Y2)
d = math.sqrt(simpleExpression)

# displaying the value
print(f"The Value of d is: {d}")


