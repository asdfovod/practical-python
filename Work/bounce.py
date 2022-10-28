# bounce.py
#
# Exercise 1.5

ballHeight = 100
bounce = 3/5

for i in range(10):
    ballHeight = ballHeight*bounce
    print(i+1, round(ballHeight, 4))
    
