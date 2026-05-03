class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:

        freq = collections.defaultdict(int)
        # The smallest card in your hand must start a group. 
        # There's no other option — nothing can come before the minimum,
        # so it has to be the beginning of some consecutive sequence.

        if len(hand) % groupSize != 0:
            return False

        for card in hand:
            freq[card] += 1

        sorted_keys = sorted(freq.keys())  # sort once
        
        for key in sorted_keys:
            count = freq[key]  # how many groups start here
            if count <= 0:
                continue       # already used up, skip
            for i in range(groupSize):
                freq[key+i] -= count  # consume all groups at once
                if freq[key+i] < 0:
                    return False

        return True