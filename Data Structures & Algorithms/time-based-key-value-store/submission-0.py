class TimeMap:

    def __init__(self):
        self.map = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        if key in self.map:
            l, r = 0, len(self.map[key])-1
            while l <= r:
                mid = l + (r-l)//2

                if self.map[key][mid][0] == timestamp:
                    return self.map[key][mid][1]
                elif self.map[key][mid][0] > timestamp:
                    r = mid - 1
                else:
                    l = mid + 1
                    res = self.map[key][mid][1]
        return res
        
