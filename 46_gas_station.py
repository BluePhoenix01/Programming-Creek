def canCompleteCircuit(gas, cost):
    if sum(gas) < sum(cost):
        return -1
    start = 0
    tank = 0
    for i in range(len(gas)):
        tank += gas[i] - cost[i]
        if tank < 0:
            start = i + 1
            tank = 0
        
    return start

print(canCompleteCircuit([1, 2, 3, 4, 5], [2, 3, 4, 5, 1]))  # Output: 4
print(canCompleteCircuit([2, 3, 4], [3, 4, 3]))  # Output: -1