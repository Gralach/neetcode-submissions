class ListNode:
    def __init__(self, val, prev = None, next = None):
        self.val = val
        self.next = next
        self.prev = prev

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        # circle = 0, square = 1
        student_queue, sandwich_queue = ListNode(-1), ListNode(-1)
        student_tail, sandwich_tail = ListNode(-1), ListNode(-1)
        st, sa = student_queue, sandwich_queue
        size, count = len(students), 0

        for student, sandwich in zip(students, sandwiches):
            st.next = ListNode(student, st)
            sa.next = ListNode(sandwich, sa)
            st, sa = st.next, sa.next

        st.next, sa.next = student_tail, sandwich_tail
        student_tail.prev, sandwich_queue.prev = st, sa
        cur_st, cur_sa = student_queue.next, sandwich_queue.next
        while cur_st and count < size:
            if cur_st.val == cur_sa.val:
                cur_st = cur_st.next
                cur_sa = cur_sa.next
                cur_st.prev, cur_sa.prev = student_queue, sandwich_queue
                size -= 1
                count = 0
            else:
                temp = cur_st
                cur_st = cur_st.next
                cur_st.prev = student_queue
                st.next = temp
                temp.prev = st
                st = st.next
                st.next = student_tail
                student_tail.prev = st
                count += 1
        return size