class TimeMap:

    def __init__(self):
        self.map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append((value, timestamp))
        

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        if key in self.map:
            arr = self.map[key]
            l, r = 0, len(arr)-1
            while l <= r:
                mid = l + (r-l)//2
                if arr[mid][1] == timestamp:
                    return arr[mid][0]
                if arr[mid][1] > timestamp:
                    r = mid - 1
                else:
                    res = arr[mid][0]
                    l = mid + 1
        return res