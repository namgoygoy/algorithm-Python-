string1 = str(input())
string2 = str(input())
result = ""
length = max(len(string1), len(string2))
for i in range(length):
    if len(string1) <= i:
        result += string2[i]
    elif len(string2) <= i:
        result += string1[i]
    else:
        result += string1[i] + string2[i]
print(result)