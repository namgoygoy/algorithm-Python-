nums = []
for i in range(1, 10):
    N = int(input())
    nums.append(N)

for idx, num in enumerate(nums):
    if num == max(nums):
        print(num)
        print(idx + 1)