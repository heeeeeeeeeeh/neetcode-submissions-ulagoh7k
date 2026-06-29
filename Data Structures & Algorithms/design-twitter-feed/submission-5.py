class Twitter:

    def __init__(self):
        self.count = 0
        self.tweetMap = defaultdict(lambda : deque(maxlen=10))
        self.followMap = defaultdict(set)
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].appendleft((self.count, tweetId))
        self.count += 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        return [tweetId for _, tweetId in islice(heapq.merge(*
            (self.tweetMap[followee] for followee in ({userId} | self.followMap[userId])),reverse=True), 10)]



    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
