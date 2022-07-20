#
# @lc app=leetcode id=142 lang=python3
#
# [142] Linked List Cycle II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# 使用两个指针，第一个走一步，第二个走两步
# 假设环的长度为r，两个指针相遇时，第一个走了k步，第二个指针走了n圈
# 假设头到环的开始节点的距离为s，环的头到相遇的距离为m
# 则 2k = k + nr => k = nr（总路程）
# s = k - m => s = nr -m => s = (n - 1)r + (r - m)
# 由上式可知，头到环的开始节点的距离 等于 整数倍环的距离 加上 相遇位置到下次环头的距离
# 换句话说，一个指针指向头，另一个指针指向相遇位置，共同推进时，必会相遇于环头
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            None
        
        fast, slow = head, head
        is_cycle = False
        while fast and fast.next and slow:
            fast = fast.next.next
            slow = slow.next    
            if fast is slow:
                is_cycle = True
                break
        if not is_cycle:
            return None
        p = head
        while p is not slow:
            p = p.next
            slow = slow.next
        return p
        
# @lc code=end

