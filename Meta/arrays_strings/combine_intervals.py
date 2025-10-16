# Combine intervals
# return list of combined intervals

# Ex. (1, 4) (3, 7) -> (1, 7)
# ()
# Combine based on start of 
# Sort by start interval
# Combine intervals
# if end > start - overlap -> combine 
# else start with a new interval
# Time sort -> O(nlogn) + O(n) -> n intervals
# Space -> O(n) to store output

def combine_intervals(intervals):
    sorted_intervals = sorted(intervals, key = lambda x: x[0])
    
    combine_intervals = [ sorted_intervals[0] ]
    #print(combine_intervals)
    for i in range(1, len(sorted_intervals)):
        if sorted_intervals[i-1][1] >= sorted_intervals[i][0]:
            #Update current interval combined to min and max of merged intervals
            combine_intervals[-1] = (min(combine_intervals[-1][0],sorted_intervals[i][0]), max(combine_intervals[-1][1], sorted_intervals[i][1])) # Update last value
        elif sorted_intervals[i-1][1] < sorted_intervals[i][0]:
            # add new interval
            combine_intervals.append(sorted_intervals[i]) # add new interval
        #print(i, combine_intervals, sorted_intervals[i])

    return combine_intervals

def combine_intervals_alt(intervals):
  sorted_intervals = sorted(intervals, key=lambda x : x[0])
  combined = [ sorted_intervals[0] ]
  
  for current_interval in sorted_intervals[1:]:
    last_start, last_end = combined[-1] # Get last interval and current interval
    current_start, current_end = current_interval
    
    if current_start <= last_end: # condition to merge
      if current_end > last_end: # do we need to update last end
        combined[-1] = (last_start, current_end)
    else:
      combined.append(current_interval)
      
  return combined

# ans1 = combine_intervals([(1, 4), (3, 7)])
# print(ans1)

ans2 = combine_intervals([(3, 7),
  (5, 8),
  (1, 5),])
print(ans2)