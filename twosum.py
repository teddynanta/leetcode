def twoSum(nums: list[int], target: int):
    result = 0 #initialize result to get into the while loop
    while(result != target): #check whether result is correct or not
        for i in range(len(nums)): 
            for j in range(1, len(nums)):
                if i == j: #check if the element is same, if yes, skip to the next element
                    continue
                result = nums[i] + nums[j] #sum two element on the list and update the result
                # print(i, j)
                # print(result)
                if result == target:
                    return [i, j] #if the result is correct, return the element index
        
            
# print(twoSum(nums = [2,5,5,11], target = 10)) #Test Code