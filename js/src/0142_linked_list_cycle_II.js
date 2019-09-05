

/**
 * 142. Linked List Cycle II.
 *
 * @see https://leetcode.com/problems/linked-list-cycle-ii/
 *
 * @param {ListNode} head
 * @return {ListNode}
 */
let detectCycle = function(head) {
    const nodes = new Set()
    while (head) {
      if (nodes.has(head)) {
        return head
      }

      nodes.add(head)
      head = head.next
    }

    return null
}
