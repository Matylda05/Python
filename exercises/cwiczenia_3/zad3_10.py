

def roman2int2(dictionary, s):
    result = 0
    i = 0
    while i < len(s):
        if i + 1 < len(s) and (dictionary[s[i]] < dictionary[s[i+1]]):
            result += dictionary[s[i+1]] - dictionary[s[i]]
            i += 2
        else:
            result += dictionary[s[i]]
            i += 1
    return result

dictionary1 = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}
letters = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
values = [1, 5, 10, 50, 100, 500, 1000]
dictionary2 = dict(zip(letters, values))

dictionary3={}
for i in range(len(letters)):
    dictionary3[letters[i]] = values[i]

ROM = "MMMDCCCLXXXVIII"
print(ROM, "=", roman2int2(dictionary1, ROM))
ROM = "MCMXCV"
print(ROM, "=", roman2int2(dictionary1, ROM))

ROM = "MMMDCCCLXXXVIII"
print(ROM, "=", roman2int2(dictionary2, ROM))
ROM = "MCMXCV"
print(ROM, "=", roman2int2(dictionary2, ROM))

ROM = "MMMDCCCLXXXVIII"
print(ROM, "=", roman2int2(dictionary3, ROM))
ROM = "MCMXCV"
print(ROM, "=", roman2int2(dictionary3, ROM))