N, M = map(int, input().split())

hour = N
min = M

if min < 45:
    if hour == 0:
        hour = 23
        min = min + 60 - 45
    else:    
        hour = hour - 1
        min = min + 60 - 45

else:
    hour = N
    min = M - 45

print(hour, min)