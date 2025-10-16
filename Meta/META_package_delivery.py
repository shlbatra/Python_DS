# Input list of start and end points and load. Give a sequence of delivery points and max capacity, can the route be finished
# Ex. [[1, 3, 4], [2, 4, 6], [3, 5, 8]] 10 -> True
# Ex. [[1, 3, 4], [2, 4, 7], [3, 5, 8]] 10 -> False

# Convert to points on line with adding load +l and reducing load -l
# Sort the points
# Keep going and have a cumulative sum

# Time complexity O(n+nlogn+2n) where n is the number of delivery pts
# Space complexity O(2n)

def can_complete_route(route, max_capacity):

    events = []

    for start, end, load in route:
        events.append((start, load))
        events.append((end, -load))

    events.sort()

    print(events)
    curr_load = 0
    for position, load_change in events:
        curr_load = curr_load + load_change
        print(curr_load)
        if curr_load > max_capacity:
            return False

    return True

ans1 = can_complete_route([[1, 3, 4], [2, 4, 6], [3, 5, 8]], 10)
print(ans1)
ans2 = can_complete_route([[1, 3, 4], [2, 4, 7], [3, 5, 8]], 10)
print(ans2)