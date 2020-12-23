def checkPossibility(nums):
    print(nums)
    non_decreasing_count = 0
    max_value = 0
    if len(nums) <3:
        return True
    for i in range(len(nums)-1):
        if max_value > 0 and i > 0:
            if nums[i+1] < max_value:
                print ("Inside 1")
                return False
        if (nums[i] > nums[i+1]):
            if i > 0:
                max_value = nums[i-1]
            non_decreasing_count += 1
            if non_decreasing_count == 2:
                print ("Inside 2")
                return False
    # if nums[-3] > nums[-1]:
    #     return False
    # print ("Inside 3")
    return True

def thirdMax(nums):
    if len(nums) <3:
        return max(nums)
    else:
        unique_nums = list(set(nums))
        unique_nums.sort()
        return (unique_nums[-3])


def canPlaceFlowers(flowerbed, n):
    plants = n

    if n == 0:
        return True

    if n = 1 and len(flowerbed) == 1 and flowerbed[0] == 0:
        return True
        
    if len(flowerbed) < (n*2-1) :
        return False

    i = 0
    if (flowerbed[i] == 0 and flowerbed[1] == 0):
        plants -= 1
        if plants == 0:
            return True 
    i += 1

    while i < len(flowerbed) - 2 :
        if (flowerbed[i-1] == 0 and flowerbed[i] == 0 and flowerbed[i+1] == 0):
            flowerbed[i] = 1
            plants -= 1
            if plants == 0:
                return True
        i += 1
    if flowerbed[-3] == 0 and flowerbed[-2] == 0 and flowerbed[-1] == 0:
        return True
    return False








