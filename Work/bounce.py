# bounce.py
#
# Exercise 1.5
bounce_height = 100 #Meters
bounce_count = 1

while bounce_count <= 10:
    bounce_height = round(bounce_height * (3/5), 4)
    print (bounce_count, round(bounce_height, 4))
    bounce_count += 1