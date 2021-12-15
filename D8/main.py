import time

start = float(round(time.time() * 1000, 5))
with open("input.txt") as data:
    data = data.readlines()

signals = [x.split(" | ") for x in data]
output = [[x.strip("\n").split(" ") for x in signals[i]] for i in range(len(signals))]
final_result = 0

for i in range(len(output)):
    l0, l1, l2, l3, l4, l5, l6, l7, l8, l9 = [],[],[],[],[],[],[],[],[],[]
    for elem in output[i][0]:

        if len(elem) == 2: l1.append(elem)
        elif len(elem) == 3: l7.append(elem)
        elif len(elem) == 4: l4.append(elem)
        elif len(elem) == 7: l8.append(elem)

    for elem in output[i][0]:
        if len(elem) == 6:
            count4 = 0
            for a in l4[0]:
                if a in elem: count4 += 1
            if count4 == 4: l9.append(elem)
            elif l1[0][0] in elem and l1[0][1] in elem: l0.append(elem)
            else: l6.append(elem)
        if len(elem) == 5:
            count4 = 0
            for a in l4[0]:
                if a in elem: count4 += 1
            if count4 == 3 and l1[0][0] in elem and l1[0][1] in elem: l3.append(elem)
            elif count4 == 3: l5.append(elem)
            elif count4 == 2: l2.append(elem)
    result = ""
    for elem in output[i][1]:
        # print(l0, l1, l2, l3, l4, l5, l6, l7, l8, l9)
        if sorted(elem) == sorted(l0[0]): result += "0"
        elif sorted(elem) == sorted(l1[0]): result += "1"
        elif sorted(elem) == sorted(l2[0]): result += "2"
        elif sorted(elem) == sorted(l3[0]): result += "3"
        elif sorted(elem) == sorted(l4[0]): result += "4"
        elif sorted(elem) == sorted(l5[0]): result += "5"
        elif sorted(elem) == sorted(l6[0]): result += "6"
        elif sorted(elem) == sorted(l7[0]): result += "7"
        elif sorted(elem) == sorted(l8[0]): result += "8"
        elif sorted(elem) == sorted(l9[0]): result += "9"
    
    result = int(result)
    final_result += result

print(final_result)
end = float(round(time.time() * 1000, 5))
result = end - start
print(f"{end - start} ms")
