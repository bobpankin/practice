def validMountainArray(arr):
    #Practice
    """
    arr.length >= 3
    There exists some i with 0 < i < arr.length - 1 such that:
    arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
    arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
    """
    if len(arr) < 3:
        return False

    peak_found = False
    i = 1

    while i <= len(arr)-2: 
        if (arr[i] == arr[i+1]):  # Flat mountain
            return False
        
        if (arr[i]<arr[i-1] and arr[i+1]>arr[i]): # Valley
            return False
    

        if (arr[i]>arr[i-1] and arr[i+1]<arr[i] and peak_found == False):
            peak_found = True # Found the peak
        elif peak_found == True:
            if arr[i] > arr[i-1]:  # Second peak
                return False 
        i+=1

    if (arr[-1] > arr[-2]): 
        return False
    
    if (peak_found == False and arr[-1] < arr[-2]):
        return False
    
    return True


def lengthOfLastWord(sentence):
    """
    Given a string s consists of some words separated by spaces, 
    return the length of the last word in the string. If the last word does not exist, 
    return 0.
    A word is a maximal substring consisting of non-space characters only.
    """
    word_array = sentence.strip().split(" ")
    return len(word_array[-1])

def runningSum(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    Given an array nums. We define a running sum of an array as 
    runningSum[i] = sum(nums[0]…nums[i]).
    Return the running sum of nums.
    """
    running_sum_array = [nums[0]]
    i = 1 
    while i < len(nums):
        running_sum_array.append(running_sum_array[i-1]+nums[i])
        i+=1
    return running_sum_array
