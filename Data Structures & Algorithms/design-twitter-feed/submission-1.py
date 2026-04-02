from collections import defaultdict
class Twitter:

    def __init__(self):
        # need to track time too
        self.tweets = defaultdict(list) #  userid -> { [tweetID1, tweetId2, ..] }
        self.followMap = defaultdict(set) # track who a user follows userID -> [followeeIds]
        self.time = 0 # track time for sorting for most recent
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        self.tweets[userId].append((self.time, tweetId))


    def getNewsFeed(self, userId: int) -> List[int]:
        # most k tweets where k = 10
        mostrecent = list(self.tweets[userId])

        # find all users a user follows and then get their tweets
        for user in self.followMap[userId]:
            if user != userId:                  # skip self to avoid duplicates
                mostrecent += self.tweets[user]

        mostrecent.sort(key=lambda x: -x[0])  # sort by time, descending
        
        return [tweetId for time, tweetId in mostrecent[:10]]

    def follow(self, followerId: int, followeeId: int) -> None:
        # You want: followerId -> set of people they follow
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        
        self.followMap[followerId].discard(followeeId)