import numpy as np
import time

# For time taking
timer = []
for _ in range(1000):
    start = float(round(time.time() * 1000, 5))
    np.set_printoptions(linewidth=np.inf)

    # Parsing data
    with open("input.txt") as data: 
        data = data.readlines()

        coordinates = [int(i) for x in data for i in x.strip("\n").split(",") if 0 < len(i) < 10]
        coordinates = [[coordinates[i], coordinates[i+1]] for i in range(0,len(coordinates),2)]

        folds = [[x.strip("\n").split(" ")[-1].split("=")[0], int(x.strip("\n").split("=")[-1])] for x in data if len(x) > 13]

    # Making map
    max_x, max_y = max(x[0] for x in coordinates), max(x[1] for x in coordinates)
    a = np.zeros((max_y + 1, max_x + 1), dtype=int)

    for i in coordinates:
        a[i[1],i[0]] = 55

    # Folding
    def folder(times, fold):
        global a
        if fold == 'y':
            A = a[times+1:]
            cord = np.where(A==55)
            new_coordinates = ((abs(times - cord[0][i] - 1), cord[1][i]) for i in range(len(cord[0])))
            a = a[:times]
            for i in new_coordinates:
                a[i[0],i[1]] = 55
        else:
            B = a[:,times+1:]
            cord = np.where(B==55)
            new_coordinates = ((cord[0][i], abs(times - cord[1][i] - 1)) for i in range(len(cord[0])))
            a = a[:,:times]
            for i in new_coordinates:
                a[i[0],i[1]] = 55

        return np.count_nonzero(a == 55)

    results = [folder(fold[1], fold[0]) for fold in folds]

    end = float(round(time.time() * 1000, 5))
    timer.append(end-start)
    # print(f"{end - start} ms")

print(f"avg time from 1000 runs is: {round(sum(timer) / len(timer), 5)} ms")