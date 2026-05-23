N = int(input())

for _ in range(N):
    M = int(input())
    li = list(map(int, input().split()))

# 퀵 정렬 구현
    # def quick_sort(arr):
    #     if len(arr) <= 1:
    #         return arr
    #     pivot = arr[len(arr)//2]  # 중앙값 피벗
    #     left  = [x for x in arr if x < pivot]
    #     mid   = [x for x in arr if x == pivot]
    #     right = [x for x in arr if x > pivot]
    #     return quick_sort(left) + mid + quick_sort(right)


    # 큰 값과 작은 값을 멀리 떨어뜨릴 수 있는 구조를 만들기 위해
    li.sort()
    max_dificult = 0

    # 원형 배치에서는 인접 관계가 정렬상 2칸 떨어진 값들에서 발생하기 때문에 최대 높이 차이는 그 값들 중 최대가 된다.
    for i in range(2, len(li)):
        dificult = 0
        dificult = li[i] - li[i-2]
        if dificult > max_dificult:
            max_dificult = dificult

    print(max_dificult)

