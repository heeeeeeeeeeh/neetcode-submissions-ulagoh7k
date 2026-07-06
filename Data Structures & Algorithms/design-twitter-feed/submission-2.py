class Twitter:

    def __init__(self):
        self.tweets = defaultdict(lambda : deque(maxlen=10))
        self.follows = defaultdict(set)
        self.count = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].appendleft((self.count, tweetId))
        self.count += 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        posts = [self.tweets[id] for id in {userId} | self.follows[userId]]
        mergedPosts = heapq.merge(*posts, reverse=True)
        return [tweetId for _, tweetId in islice(mergedPosts, 10)]
        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.follows[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follows[followerId]:
            self.follows[followerId].remove(followeeId)
        
