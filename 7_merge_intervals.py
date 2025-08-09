def mergeIntervals(intervals):
    if not intervals:
        return []
    intervals.sort(key=lambda x: x[0])
    merged = []
    start = intervals[0][0]
    end = intervals[0][1]
    for i in range(1, len(intervals)):
        if intervals[i][0] <= end:
            end = max(end, intervals[i][1])
        else:
            merged.append([start, end])
            start = intervals[i][0]
            end = intervals[i][1]
    merged.append([start, end])
    return merged
    
print(mergeIntervals([[1,3],[2,6],[8,10],[15,18]]))
    