class Twitter:

    def __init__(self):
        self.count = 1
        self.tweetMap = defaultdict(lambda : deque(maxlen=10))
        self.followMap = defaultdict(set)
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].appendleft((self.count, tweetId))
        self.count += 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        posts = (self.tweetMap[followeeId] for followeeId in ({userId} | self.followMap[userId]))
        heap = heapq.merge(*posts, reverse=True)
        return [tweetId for _, tweetId in islice(heap, 10)]
        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.followMap[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
