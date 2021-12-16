
with open("input.txt") as data:
    data = data.read()

# Hexadecimal representation
rep = {
"0":"0000",
"1":"0001",
"2":"0010",
"3":"0011",
"4":"0100",
"5":"0101",
"6":"0110",
"7":"0111",
"8":"1000",
"9":"1001",
"A":"1010",
"B":"1011",
"C":"1100",
"D":"1101",
"E":"1110",
"F":"1111"
}

# Hexadecimal string to binary
binary = ""
for char in data:
    binary += char.replace(char, rep[char])
# print(binary)

sum_of_versions = 0
def recursio(binary):
    global sum_of_versions
    version = int(binary[:3], 2)
    sum_of_versions += version
    binary = binary[3:]
    
    type_ID = int(binary[:3], 2)
    binary = binary[3:]
    if type_ID == 4:
        num = ""
        while True:
            num += binary[1:5]
            f_num = binary[0]
            binary = binary[5:]
            if f_num == "0":
                break
        return(binary, int(num, 2))
    else:
        ltype_ID = binary[0]
        binary = binary[1:]
        subs_values = []
        if ltype_ID == "0":
            sub_length = int(binary[:15], 2)
            binary = binary[15:]
            subs = binary[:sub_length]
            while subs:
                subs, x = recursio(subs)
                subs_values.append(x)
            binary = binary[sub_length:]
        else:
            sub_length = int(binary[:11], 2)
            binary = binary[11:]
            for i in range(sub_length):
                binary, x = recursio(binary)
                subs_values.append(x)
        print(subs_values)
        if type_ID == 0:
            return (binary, sum(subs_values))
        if type_ID == 1:
            product = 1
            for i in subs_values:
                product *= i
            return (binary, product)
        if type_ID == 2:
            return (binary, min(subs_values))
        if type_ID == 3:
            return (binary, max(subs_values))
        if type_ID == 5:
            return (binary, 1 if subs_values[0] > subs_values[1] else 0)
        if type_ID == 6:
            return (binary, 1 if subs_values[0] < subs_values[1] else 0)
        if type_ID == 7:
            return (binary, 1 if subs_values[0] == subs_values[1] else 0)
    
print(recursio(binary)[1])