
with open("input.txt") as data:
    data = data.readlines()
data = [x.strip("\n") for x in data]
# print(data)

# -------------------- PART 1 --------------------------
# gamma = ""
# for i in range(len(data[0])):
#     zeros, ones = 0, 0
   
#     for binary in data:
#         if binary[i] == "0":
#             zeros += 1
#         else: ones += 1
#     if ones > zeros: gamma += "1"
#     else: gamma += "0"

# print(gamma)
# epsilon = ""
# for i in gamma:
#     if i == "0": epsilon += "1"
#     else: epsilon += "0"

# gamma = int(gamma, 2)
# epsilon = int(epsilon, 2)
# print(gamma, epsilon, gamma * epsilon)

# ------------------- PART 2 ---------------------

# print(data)

oxygen_generator_rating = data.copy()

for i in range(len(data[0])):
    zeros, ones, zero_list, one_list = 0, 0, [], []
    if len(oxygen_generator_rating) == 1: break
    for binary in oxygen_generator_rating:
        if binary[i] == "0": zeros += 1; zero_list.append(binary)
        else: ones += 1; one_list.append(binary)
    if ones >= zeros: 
        for elem in zero_list:
            oxygen_generator_rating.remove(elem)
    else:
        for elem in one_list:
            oxygen_generator_rating.remove(elem)
print(oxygen_generator_rating)

CO2_scrubber_rating = data.copy()

for j in range(len(data[0])):
    zero, one, zeros_list, ones_list = 0, 0, [], []
    if len(CO2_scrubber_rating) == 1: break
    for binary2 in CO2_scrubber_rating:
        if binary2[j] == "0": zero += 1; zeros_list.append(binary2)
        else: one += 1; ones_list.append(binary2)    
    if zero <= one: 
        for element in ones_list:
            CO2_scrubber_rating.remove(element)
    elif one < zero:
        for element in zeros_list:
            CO2_scrubber_rating.remove(element) 
print(CO2_scrubber_rating)


OGR = int(oxygen_generator_rating[0], 2)
CO2sr = int(CO2_scrubber_rating[0], 2)
print(CO2sr, OGR, CO2sr * OGR)
