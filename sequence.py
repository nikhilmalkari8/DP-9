def lengthOfLIS(nums):
    if not nums:
        return 0
    
    # DP array to store the length of the LIS ending at each index
    dp = [1] * len(nums)
    
    # Loop through each element in the list
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    # The answer is the maximum value in the dp array
    return max(dp)
