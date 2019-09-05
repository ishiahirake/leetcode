

/**
 * 141. Linked List Cycle.
 *
 * @see https://leetcode.com/problems/linked-list-cycle/
 *
 * @param {ListNode} head
 * @return {boolean}
 */
let hasCycle = function(head) {
  let [fast, slow] = [head, head]
  while (fast && fast.next) {
    slow = slow.next
    fast = fast.next.next
    if (fast === slow) {
      return true
    }
  }

  return false
}
