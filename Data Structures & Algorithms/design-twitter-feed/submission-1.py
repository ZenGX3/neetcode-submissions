class Twitter:

    def __init__(self):
        self.d = {}
        self.d1 = {}
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1

        if userId not in self.d:
            self.d[userId] = []

        heapq.heappush_max(self.d[userId], (self.time, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        h = []

        # User's own tweets
        if userId in self.d:
            for tweet in self.d[userId]:
                heapq.heappush_max(h, tweet)

        # Followed users' tweets
        if userId in self.d1:
            for followee in self.d1[userId]:
                if followee in self.d:
                    for tweet in self.d[followee]:
                        heapq.heappush_max(h, tweet)

        ans = []

        for i in range(min(len(h), 10)):
            ans.append(heapq.heappop_max(h)[1])

        return ans

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return

        if followerId not in self.d1:
            self.d1[followerId] = set()

        self.d1[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.d1:
            self.d1[followerId].discard(followeeId)