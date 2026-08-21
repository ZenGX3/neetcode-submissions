class Solution:
    def isNStraightHand(self, hand: List[int], gSz: int) -> bool:
        d = {}
        if len(hand)%gSz:
            return False
        
        for x in hand:
            d[x] = 1 + d.get(x, 0)
        mH = list(d.keys())
        heapq.heapify(mH)
        while mH:
            n = mH[0]
            for i in range(n, n + gSz):
                if i not in d:
                    return False
                d[i] -= 1
                if d[i] == 0:
                    if i != mH[0]:
                        return False
                    heapq.heappop(mH)
        return True

        
        