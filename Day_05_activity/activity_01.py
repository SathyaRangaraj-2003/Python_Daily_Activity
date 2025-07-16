# Print Only the Middle Digit of a 3-digit Number Scenario: Given a 3-digit number x = 426, print only the middle digit. 

#soln 01
x=426
y=str(x)
print(y[1:2])

#soln 02
print((x // 10) % 10)
