# bounce.py
#
# Exercise 1.5
def trackHeight(time):
    i = 1
    height = 100
    while time >= i:
        print(i, end=" ")
        height = height * 0.6
        print(round(height, 4))
        i = i + 1

trackHeight(10)