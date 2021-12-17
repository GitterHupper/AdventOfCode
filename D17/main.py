from itertools import product

with open("input.txt") as data:
    trajectory = data.readline().strip("target area: x=").split(", y=")
    landing = [[int(x) for x in i.split("..")] for i in trajectory]


highest_y, possible_angles = 0, []
def calculate_landing(starting_xvalue, starting_yvalue):
    global highest_y, possible_angles

    x, y = starting_xvalue, starting_yvalue
    curr_xpos, curr_ypos, top_y = 0, 0, 0

    while y > -500:
        if y > 0: top_y += y

        curr_xpos += x
        curr_ypos += y
        if x > 0: x -= 1
        elif x < 0: x += 1
        else: x = 0
        y -= 1

        if min(landing[0]) <= curr_xpos <= max(landing[0]) and min(landing[1]) <= curr_ypos <= max(landing[1]):
            return True
            if top_y > highest_y:
                highest_y = top_y    

        if y < -1000:
            break

# x probably coming staright down | part 1
k, summed, highest_change = 0, 0, []
while summed <= max(landing[0]):
    k += 1
    summed += k
    if min(landing[0]) <= summed <= max(landing[0]):
        highest_change.append(k)

# Brute helvetti
for x,y in product(range(-50,294), range(-250,250)):
    if calculate_landing(x, y):
        possible_angles.append((x,y))

print(highest_y, len((possible_angles)))
