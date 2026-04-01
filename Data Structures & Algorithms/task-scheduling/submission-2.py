class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # all tasks take the same amount of time
        # same tasks have to be seperated by n
        # makes sense to do the most freq occuring tasks first -> greedy
        # heap of (freq, task)
        # need to keep track of which one is the most freq at any given time

        freq = defaultdict(int)

        for task in tasks:
            freq[task] += 1

        cpu_cycles = 0

        maxheap = []

        for task, frequency in freq.items():
            heapq.heappush(maxheap, (-frequency) )

        q = deque()
        ### start calculating cycles

        while maxheap or q:
            
            if q and q[0][1] == cpu_cycles:
                freq , _ = q.popleft()
                heapq.heappush(maxheap, -freq)
                
            if maxheap:
                freq = heapq.heappop(maxheap)

                freq *= -1 # restore it to positive number

                freq -= 1
                ### now how to track cooldown of this task that was just completed?    
                if freq > 0:
                    q.append((freq,cpu_cycles + n +1))



            cpu_cycles += 1

        return cpu_cycles
