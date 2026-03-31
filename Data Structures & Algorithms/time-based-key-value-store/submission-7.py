class TimeMap:

    def __init__(self):
        self.map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        
        if key in self.map:
            self.map[key].append((value, timestamp))
        else:
            self.map[key] = [(value,timestamp)]

    def get(self, key: str, timestamp: int) -> str:
        # look for this timestamp within the key
        if key in self.map:
            keylist = self.map[key]
        else:
            return ""
        #### [ (happy, 1), (sad , 3), (excited, 6)]

        l, r = 0, len(keylist) -1
        mostrecent = 0
        while l <= r:
            mid = (l+r)//2
            if keylist[mid][1] <= timestamp:
                mostrecent = keylist[mid]
                l = mid + 1 # search right for more recent one

            else:
                r = mid - 1 # too new, search left

        if not mostrecent:
            return ""
        else:
            return mostrecent[0]
        

                