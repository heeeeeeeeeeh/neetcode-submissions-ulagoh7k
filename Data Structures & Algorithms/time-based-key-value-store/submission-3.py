class TimeMap:

    def __init__(self):
        self.map = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append((value,timestamp))

    def get(self, key: str, timestamp: int) -> str:
        res, item = "", self.map[key]
        l, r = 0, len(item)-1

        while l <= r:
            mid = l + (r-l)//2

            if item[mid][1] == timestamp:
                return item[mid][0]
            elif item[mid][1] < timestamp:
                res = item[mid][0]
                l = mid + 1
            else:
                r = mid - 1
        return res