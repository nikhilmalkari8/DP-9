import bisect

def maxEnvelopes(envelopes):
    # Sort the envelopes: first by width, and then by height (descending if widths are equal)
    envelopes.sort(key=lambda x: (x[0], -x[1]))
    
    # Extract the heights from the sorted envelopes
    heights = [h for _, h in envelopes]
    
    # Find the length of the longest increasing subsequence of heights
    tails = []
    for height in heights:
        # Find the position where the height should be placed in the tails array
        pos = bisect.bisect_left(tails, height)
        
        # If pos is equal to the length of tails, it means we can append this height
        if pos == len(tails):
            tails.append(height)
        else:
            # Otherwise, replace the element at pos with the current height
            tails[pos] = height
    
    # The length of tails is the length of the LIS
    return len(tails)
