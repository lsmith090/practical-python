# bounce.py
#
# Exercise 1.5
bounce_height = 100 #Meters
bounce_count = 0

while bounce_count <= 10:
    bounce_height = bounce_height * (3/5)
    print (bounce_count, round(bounce_height, 4))
    bounce_count += 1