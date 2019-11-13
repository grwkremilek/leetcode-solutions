#https://leetcode.com/problems/kth-largest-element-in-an-array/


def findKthLargest(nums, k):
    return sorted(nums)[-k]
        

def findKthLargest(nums, k):
    pq = nums[:k]
    heapq.heapify(pq)
    for x in nums[k:]:
        heapq.heappush(pq, x)
        heapq.heappop(pq)
    return pq[0]

